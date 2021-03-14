from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, AnyUrl


class Adr(BaseModel):
    type: str
    value: str


class Label(BaseModel):
    type: str
    value: str


class Related(BaseModel):
    type: str
    value: str


class Tel(BaseModel):
    type: str
    value: str


class Photo(BaseModel):
    # TODO create photo field
    pass

