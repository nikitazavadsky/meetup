from data.EntityHandler import (Meetup, Params)

AVAILABLE_API_ENTITIES = [Meetup, Params]

# Map `entity : endpoint name`
ENDPOINT_MAP = {
    Meetup: 'meetups',
    Params: 'params'
}
