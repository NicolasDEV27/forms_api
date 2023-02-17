from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    DNI: Optional[int] = None
    Name: str = Field(min_length=1, max_Length=20)
    Last_names: str = Field(min_length=1, max_Length=20)
    Age: int = Field(ge=1, le=100)
    Height: float = Field(ge=0.1, le=2.5)
    Birthday:  str = Field(min_Length=10, max_length=10)
    email: str = Field(min_length=1, max_Length=20)
    password: str = Field(min_length=1, max_Length=20)

  