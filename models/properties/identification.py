from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, AnyUrl


class FN(BaseModel):
    pass


class N(BaseModel):
    pass


class Nickname(BaseModel):
    pass


class Photo(BaseModel):
    pass


class Bday(BaseModel):
    pass


class Anniversary(BaseModel):
    pass


class Gender(BaseModel):
    pass
