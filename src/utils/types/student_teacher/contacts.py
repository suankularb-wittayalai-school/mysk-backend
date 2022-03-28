from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date
from enum import Enum, IntEnum


class ContactType(str, Enum):
    """
    Contact type
    """

    Phone = "Phone"
    Email = "Email"
    Facebook = "Facebook"
    Line = "Line"
    Instagram = "Instagram"
    Website = "Website"
    Discord = "Discord"
    Other = "Other"


class Contact(BaseModel):
    id: str
    name: str
    type: ContactType
    value: str
