from abc import ABC, abstractmethod
from pydantic import ValidationError

from data.models import (RsvpMeetup, Params)
from constants import (AVAILABLE_API_ENTITIES, ENDPOINT_MAP)


class EntityConverter(ABC):

    @staticmethod
    @abstractmethod
    def get_entity(content): pass

    def convert(self, content):
        """Method converts content to entity / list of entities"""

        entities = content.get('entities')
        if entities:
            if isinstance(entities, list):
                entities_list = []
                for entity_dict in entities:
                    entities_list.append(self.get_entity(content=entity_dict))
                return entities_list
            return self.get_entity(content=entities)
        return []


class MeetupConverter(EntityConverter):

    @staticmethod
    def get_entity(content):
        title = content.get('title')
        description = content.get('description')
        date = content.get('date')

        try:
            response_obj = RsvpMeetup(title=title,
                                      description=description,
                                      date=date)
        except ValueError as e:
            raise ValidationError("Not valid entity", e)

        return response_obj


class ParamsConverter(EntityConverter):

    @staticmethod
    def get_entity(content):
        keywords = content.get("keywords")
        date = content.get("date")

        try:
            response_obj = Params(keywords=keywords,
                                  date=date)
        except ValueError as e:
            raise ValidationError("Not valid entity", e)

        return response_obj


class EntityConverterHandler:

    @staticmethod
    def get_entity_converter(target):
        for entity in AVAILABLE_API_ENTITIES:
            if ENDPOINT_MAP.get(entity) == target:
                return entity

        raise Exception(f'There is no entity for endpoint {target}!')
