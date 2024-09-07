from pydantic import BaseModel
from datetime import datetime


class Employee(BaseModel):
    name: str
    age: int
    hire_date: datetime
    salary: float
    position: str
