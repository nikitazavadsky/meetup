from data.models import (RsvpMeetup, Params)

AVAILABLE_API_ENTITIES = [RsvpMeetup, Params]

# Map `entity : endpoint name`
ENDPOINT_MAP = {
    RsvpMeetup: 'meetups',
    Params: 'params'
}

TEST_UNIT_DATA_DIR = 'tests/unit/test_data'
