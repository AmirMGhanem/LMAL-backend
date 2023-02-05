from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .user import User
from .address import Address


class Customer(BaseModel):
    user : User
    address : Address
    seniority : Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")