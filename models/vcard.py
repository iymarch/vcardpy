from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, AnyUrl
from models.fields import Adr, Label, Related, Tel


class VCardBase(BaseModel):
    version: str
    end: str
    begin: str
    adr: Optional[List[Adr]] = None
    bday: Optional[int] = None
    categories: Optional[str] = None
    email: Optional[EmailStr] = None
    geo: Optional[str] = None
    key: Optional[str] = None
    label: Optional[List[Label]] = None
    logo: Optional[str] = None
    note: Optional[str] = None
    org: Optional[str] = None
    photo: Optional[str] = None 
    rev: Optional[str] = None
    role: Optional[str] = None
    sound: Optional[str] = None
    source: Optional[AnyUrl] = None
    tel: Optional[List[Tel]] = None
    title: Optional[str] = None
    tz: Optional[str] = None
    uid: Optional[str] = None
    url: Optional[AnyUrl] = None


class VCardv2(VCardBase):
    n: str
    agent: Optional[AnyUrl] = None
    fn: Optional[str] = None
    mailer: Optional[str] = None
    profile: Optional[str] = None
    

class VCardv3(VCardBase):
    n: str
    fn: str
    class_type: Optional[str] = None
    agent: Optional[AnyUrl] = None
    name: Optional[str] = None
    nickname: Optional[str] = None
    Optional[str] = None
    mailer: Optional[str] = None
    prodid: Optional[str] = None
    profile: Optional[str] = None
    sort_string: Optional[str] = None


class VCardv4(VCardBase):
    fn: str
    n: Optional[str] = None
    xml: Optional[str] = None
    anniversary: Optional[int] = None
    caladruri: Optional[AnyUrl] = None
    gender: Optional[str] = None
    member: Optional[str] = None
    impp: Optional[str] = None
    kind: Optional[str] = None
    lang: Optional[str] = None
    prodid: Optional[str] = None
    related: Optional[List[Related]] = None
    nickname: Optional[str] = None
    caluri: Optional[AnyUrl] = None
    clientpidmap: Optional[str] = None
    fburl: Optional[AnyUrl] = None
    sort_string: Optional[str] = None