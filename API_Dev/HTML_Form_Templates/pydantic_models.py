from pydantic import BaseModel

class User(BaseModel):
    name_: str
    key_: int