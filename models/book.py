from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    title: str
    author: str
    year: datetime
    category: str
