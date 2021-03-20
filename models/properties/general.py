from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, AnyUrl


class Begin(BaseModel):
    pass


class End(BaseModel):
    pass


class Source(BaseModel):
    pass


class Kind(BaseModel):
    pass


class XML(BaseModel):
    pass