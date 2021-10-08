"""This module uses pydantic to perform data type checks within the Meetup application"""

import datetime

from pydantic import (BaseModel, validator)


def convert_date(cls, date):
    """Reusable validator for date conversion"""

    if not date:
        raise ValueError(f"Date must not be a null")
    else:
        try:
            return date.strftime("%Y-%m-%d %H:%M")
        except ValueError as e:
            raise Exception("Date validation error")


class Credentials(BaseModel):
    """This model represents user credentials to access API"""
    token: str


class RequestResponse(BaseModel):
    """This model represents response from the API"""
    entities: list


class RsvpMeetup(BaseModel):
    """This model represents Meetup entity"""
    title: str
    description: str
    date: datetime.datetime

    _converted_date = validator('date', allow_reuse=True)(convert_date)


class Params(BaseModel):
    """This model represents parameter for filtering"""

    keywords: list
    date: datetime.datetime

    _converted_date = validator('date', allow_reuse=True)(convert_date)


class RsvpDecision(BaseModel):
    target: RsvpMeetup
    decision: bool
