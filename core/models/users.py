from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: str
    name: str
    status: str
    created_timestamp: datetime
    updated_timestamp: datetime
