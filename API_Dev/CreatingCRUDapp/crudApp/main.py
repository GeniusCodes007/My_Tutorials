import sqlalchemy.exc
from fastapi import FastAPI, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from starlette import status
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

from .models import Users, CreatePost, UpdatePost, UserRegInfo

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        connect = psycopg2.connect(host='localhost', database='myCRUDapp',
                                   user='postgres', password='GeniusUnn#07',
                                   cursor_factory=RealDictCursor)
        cursor = connect.cursor()
        print("Database Connected!!!")
        break
    except Exception as error:
        print(f"Connection Failed!!!  \nIssue: {error}")
        time.sleep(3)

@app.get("/sqlalchemy")
def test_db(db: Session = Depends(get_db)):
    response = db.query(models.Users).all()
    return {"data": response}

@app.get("/posts")
def get_all_posts(db:Session= Depends(get_db)):
    response = db.query(models.Users).all()
    return response

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=models.Our_Response)
def create_a_post(my_posts: CreatePost, db: Session= Depends(get_db)):
    #The syntax below seems a lot stressful
    #so, we are discarding this syntax
    """new_post = models.Users(
        Title= my_posts.Title,
        Content= my_posts.Content,
        Username= my_posts.Username
    )"""
    try:
    #we are going to convert 'my_posts' to a dictionary
    #then unpack it
        if sqlalchemy.exc.IntegrityError:
            my_posts.id_ = my_posts.id_ + 1
        new_post = models.Users(
            **my_posts.model_dump()
        )
        print(my_posts.id_)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
    except Exception as e:
        return e

@app.get("/post/{id_}")
def get_one_post(id_: int, db:Session= Depends(get_db)):
    response = db.query(Users).filter(Users.id_ == id_).first()

    if response is not None:
        return response
    else:
        return "Record Not Found"

@app.delete("/post/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id_:int, db: Session= Depends(get_db)):
    response = db.query(Users).filter(Users.id_ == id_)


    if response.first() is not None:
        response.delete(synchronize_session = False)
        db.commit()
        return f"Post ID {id_} Deleted"
    else:
        return f"Post ID {id_} Not Found"

@app.get("/last play time/{hours}/{minutes}/{sec}")
async def last_video_play_time(hours: int, minutes: int, sec: int):
    return f"{hours} : {minutes} : {sec}"

@app.put("/post/{id_}", response_model=models.UpdatePost)
def update(id_:int, new_post: UpdatePost, db:Session=Depends(get_db)):
    post_query= db.query(models.Users).filter(models.Users.id_ == id_)
    post = post_query.first()

    if post is None:
        return "Not Found"
    post_query.update(new_post.model_dump() ,
                      synchronize_session=False)
    db.commit()
    return post_query.first()

@app.post("/user", status_code=status.HTTP_201_CREATED, response_model= UserRegInfo)
async def create_post( user:models.CreateUser,db: Session= Depends(get_db)):
    new_user = models.UserAccount(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user