#uvicorn api_base_file: api --reload
from fastapi import FastAPI
from typing import List
from models_file import User, Gender, Role
from uuid import uuid4


api = FastAPI()


db: List[User] = [
    User(
        id = uuid4(),
        firstName="Okechukwu",
        lastName="Ifeanacho",
        middleName= "Caius",
        fullName = f"You Know, I'm Good",
        gender = Gender.male,
        role=[Role.student],
    ),
    
    User(
        id= uuid4(),
        firstName="Genius",
        lastName="Codes",
        fullName = f"me",
        gender=Gender.male,
        role=[Role.user, Role.admin],       
    ),
]



@api.get("/")
async def root():
    return {"Hello": "Mundo"}


@api.get("/api/users")
def fetch_users():
    our_users = ()
    count = 0
    for user in db:
        #print(user)
        our_users += (count, user, "", "")
        count += 1
    #print(our_users)
    return db[0], db[1]