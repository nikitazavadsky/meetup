import datetime

from abc import ABC, abstractmethod
from pydantic import ValidationError

from data.DataModels import RsvpMeetup
from constants import (AVAILABLE_API_ENTITIES, ENDPOINT_MAP)


class EntityConverter(ABC):

    @staticmethod
    @abstractmethod
    def convert(content): pass


class MeetupConverter(EntityConverter):

    @staticmethod
    def init_entity(content):
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

    def convert(self, content):
        """Method converts content to entity / list of entities"""

        entities = content.get('entities')
        if entities:
            if isinstance(entities, list):
                entities_list = []
                for entity_dict in entities:
                    entities_list.append(self.init_entity(content=entity_dict))
                return entities_list
            return self.init_entity(content=entities)


class ParamsConverter(EntityConverter):

    @staticmethod
    def convert(content):
        return


class EntityConverterHandler:

    @staticmethod
    def get_entity_converter(target):
        for entity in AVAILABLE_API_ENTITIES:
            if ENDPOINT_MAP.get(entity) == target:
                return entity

        raise Exception(f'There is no entity for endpoint {target}!')
