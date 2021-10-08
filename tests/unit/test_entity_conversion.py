import json
import os

from constants import TEST_UNIT_DATA_DIR
from data.entity_handler import (MeetupConverter, ParamsConverter)
from data.models import (RsvpMeetup, Params)


def test_empty_response_conversion():

    expected_entities = []

    with open(os.path.join(TEST_UNIT_DATA_DIR, 'empty_entity_response.json')) as file:
        data = json.load(file)

    converter = MeetupConverter()
    entities = converter.convert(data)

    assert expected_entities == entities


def test_response_conversion_meetup():

    example_meetup = RsvpMeetup(title="Meetup",
                                description="Come here!",
                                date="2021-02-18 21:00")

    expected_entities = [example_meetup, example_meetup]

    with open(os.path.join(TEST_UNIT_DATA_DIR, 'meetup_response.json')) as file:
        data = json.load(file)

    converter = MeetupConverter()
    entities = converter.convert(data)

    assert expected_entities == entities


def test_response_conversion_params():

    example_meetup = Params(keywords=["DE", "Spark"],
                            date="2021-02-18 21:00")

    expected_entities = [example_meetup]

    with open(os.path.join(TEST_UNIT_DATA_DIR, 'params_response.json')) as file:
        data = json.load(file)

    converter = ParamsConverter()
    entities = converter.convert(data)

    assert expected_entities == entities
