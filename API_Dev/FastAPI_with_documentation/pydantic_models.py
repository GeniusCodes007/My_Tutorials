from pydantic import BaseModel, Field

from typing import List

class BooksAndAuthor(BaseModel):
    surname: str

    firstName: str

    books: List[str]

    publishers: List[str]

class Student(BaseModel):
    name:str

    age:int=Field(None, lt=30)