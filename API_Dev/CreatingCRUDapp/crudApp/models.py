from typing import Optional
from datetime import datetime
from .database import Base
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from pydantic import BaseModel, EmailStr


class Users(Base):
    __tablename__ = 'app_users'

    id_ = Column(Integer, primary_key=True, nullable= False)
    Title = Column(String(20), nullable=False)
    Content = Column(String, nullable=False)
    Username = Column(VARCHAR(12), nullable=True)
    Verified = Column(Boolean, server_default='True')
    Created_On = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))


class CreatePost(BaseModel):
    Title: str
    Content: str
    Username:str
    id_:Optional[int]
    Created : datetime = datetime.now()

    class Config:
        orm_mode = True

class UpdatePost(BaseModel):
    Title: str
    Content: str

    class Config:
        orm_mode = True

class Our_Response(BaseModel):

    class Config:
        orm_mode = True

class UserAccount(Base):
    __tablename__ = "users_account"

    id_ = Column(Integer, primary_key= True, nullable = False)
    username=Column(String(20), nullable= False, unique=True, primary_key=True)
    email= Column(String, nullable=False, unique=True)
    pin=Column(String(length=6), nullable=False)
    created_on = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))

class CreateUser(BaseModel):
    username : str
    email : EmailStr
    pin : str

class UserRegInfo(BaseModel):
    id_: int
    email: EmailStr
    username: str

    class Config:
        orm_mode=True