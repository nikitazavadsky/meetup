"""This module uses pydantic to perform data type checks within the Meetup application"""

import datetime

from pydantic import (BaseModel, validator)


class Credentials(BaseModel):
    """This model represents user credentials to access API"""
    token: str


class GetRequest(BaseModel):
    """This model represents request to the API"""
    url: str
    credentials: Credentials
    target: str


class RequestResponse(BaseModel):
    """This model represents response from the API"""
    code: int
    title: str
    description: str

    @validator('code')
    def code_must_be_200(cls, code):
        """This check verify response code to be OK only"""
        if code != 200:
            raise ValueError(f"Response is not OK but {code}")
        return code


class RsvpMeetup(BaseModel):
    """This model represents response from the API"""
    title: str
    description: str
    date: datetime.date


class RsvpDecision(BaseModel):
    target: RsvpMeetup
    decision: bool
