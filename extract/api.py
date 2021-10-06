import requests
import json


from pydantic import ValidationError

from data.DataModels import RequestResponse
from data.EntityHandler import EntityConverterHandler


class API:

    def __init__(self, host, credentials):
        self.host = host
        self.credentials = credentials

    def __generate_header(self):
        return {'Authorization': 'token {}'.format(self.credentials.token)} if self.credentials else {}

    @staticmethod
    def __is_response_ok(code):
        """This check verify response code to be OK only"""
        if code != 200:
            raise ValueError(f"Response is not OK but {code}")
        return True

    @staticmethod
    def get_entity(content):
        title = content.get('title')
        description = content.get('description')
        date = content.get('date')

        try:
            response_obj = RequestResponse(title=title,
                                           description=description,
                                           date=date)
        except ValueError as e:
            raise ValidationError("Not valid entity", e)

        return response_obj

    def content_to_entities(self, content):
        """Method converts content to entity / list of entities"""

        entities = content.get('entities')
        if entities:
            if isinstance(entities, list):
                entities_list = []
                for entity_dict in entities:
                    entities_list.append(self.get_entity(content=entity_dict))
                return entities_list
            return self.get_entity(content=entities)

    def get(self, endpoint):
        """Method uses requests and some parameters to get entities from the API"""

        url = '/'.join([self.host, endpoint])
        header = self.__generate_header()

        response = requests.get(url=url,
                                headers=header)

        self.__is_response_ok(code=response.status_code)

        response_data = json.loads(response.text)

        entity_converter = EntityConverterHandler().get_entity_converter(target=endpoint)
        entities = entity_converter().convert(content=response_data)

        return entities
