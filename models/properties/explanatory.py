from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, AnyUrl


class Categories(BaseModel):
    pass


class Note(BaseModel):
    pass


class Prodid(BaseModel):
    pass


class Rev(BaseModel):
    pass


class Sound(BaseModel):
    pass


class UID(BaseModel):
    pass


class Clientpidmap(BaseModel):
    pass


class URL(BaseModel):
    pass


class Version(BaseModel):
    pass
