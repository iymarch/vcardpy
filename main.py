import re
from copy import copy
from typing import BinaryIO

from models.vcard import VCardv2, VCardv3, VCardv4
from models.fields import Adr, Label, Related, Tel


class VCardReader:
    def __init__(self, vcard_file: BinaryIO):
        self.vcard_file = vcard_file
        self.vcard_attrs = ['ADR' 'AGENT', 'ANNIVERSARY', 'BDAY', 'BEGIN', 'END',
            'CALADRURI', 'CALURI', 'CATEGORIES', 'CLASS', 'CLIENTPIDMAP', 'EMAIL', 
            'FBURL', 'FN', 'GENDER', 'GEO', 'IMPP', 'KEY', 'KIND', 'LABEL', 'LANG', 'LOGO',
            'MAILER', 'MEMBER', 'N', 'NAME', 'NICKNAME', 'NOTE', 'ORG', 'PHOTO', 'PRODID',
            'PROFILE', 'RELATED', 'REV', 'ROLE', 'SORT_STRING', 'SOUND', 'SOURCE', 'TEL',
            'TITLE', 'TZ', 'UID', 'URL', 'VERSION', 'XML']

    def to_json(self):
        pass

    def to_xml(self):
        pass

    def to_csv(self):
        pass

    def to_dict(self):
        pass

    def to_list(self):
        pass