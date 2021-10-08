import requests
import json


from pydantic import ValidationError

from data.entity_handler import EntityConverterHandler


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
