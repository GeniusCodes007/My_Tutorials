#uvicorn api_documentation_file:app --reload
#http://127.0.0.1:8000
#"C:\API DEV\.venv\Scripts\activate.bat"
#https://www.postman.com/validate-email?token=73f2d9cebb0ee00f4bc04b89b9080951

#postman://auth/callback?code=dff493ffd9ff9175a6a1924e0c90b51a83bf0252120bc8f1b43282f4d4b1689d
"""
{
    "student name": "",
    "student reg no": ""
}
"""
"""
{
    "message": "Today's Date and Time Now",
    "date": "Today's Date",
    "time": "Time Now"
}
"""

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
#from advanced_basic_methods import AdvancedBasicMethods, EssentialMethods
#from basic_frequent_functions import BasicFrequentFunctions
import datetime


app = FastAPI()


now = datetime.datetime.now()

time_ = f"Time: {now.strftime('%H:%M:%S')}"
date_ = f"Date: {now.strftime('%Y-%m-%d')}"

num1 = 30
num2 = 144

"""
We would be using the pydantic library. 
It would be needed for the passing of parameters which we would need.
"""

# To request: we use the get method in fastapi to get some kind of information we need

@app.get("/")
async def first_experience():
    return [
        (
            f"Running APIs With Python Can Really Be Fun",
            f"",
            f"To create a function to get some information from a system, we are going to need to use the '@app.get' decorator",
            f"",
            f"In the above example, '/' and whatever that follows after that gives a reference to the data we hope to get or retrieve.",
            f"",
            f"If nothing follows '/' then '/' is the reference in our api file.",
            f"",
            f"The same things apply to '@app.post' decorator and so on, ",
            f"",
            f"Also, note that the '@app.' used here is because 'app' is the variable containing the class 'FastApi()' in this document."
        )
    ]

@app.get("/uvicorn run info")
def some_info():
    return [
        (
            f"  uvicorn api_documentation_file:app, is for loading the api",
            f"  uvicorn api_documentation_file:app --reload, is for reloading and making changes to the api at every point in time, "
            f"this done automatically"
        )
        ]

@app.get("/student details")
def studentInfo():
    return [
        {
            "student name": "Ifeanacho Okechukwu",
            "reg. no": "4588",
            "Level": 300
        },

        {
            "student name": "Genius Codes",
            "reg. no": "7452",
            "Level": 200
        },

        {
            "student name": "Genius Dexter",
            "reg. no" : "7436",
            "Level": 200
        },

        {
            "lecturer name": "Mr. Ejikeme",
            "category": "Senior",
            "department": "comp. sci."
        }
    ]


@app.post("/create post")
def createPost():
    numOfPost =+ 1
    if numOfPost > 1:
        remark = f"{numOfPost} Posts Created"
    else:
        remark = f"{numOfPost} Post Created"
    return {f"{remark}"}


#Using Body from fastapi.params

@app.get("/getting date and time")
def dateAndTime(statement: dict = Body(...)):
    statement['time'] = f"{time_}"
    statement['date'] = f"{date_}"

    return [
        (
            f"{statement['message']}",
             f"Date: {statement['date']}",
             f" Time: {time_}",
        )
    ]

@app.post("/a knowing")
def know(message: dict = Body(...)):
    return [
        (
        f"Message Title: {message['title']}",
        f"Message Content: {message['content']} ",

        )
        ]

@app.post("/testing stuff")
def stuff(test_result: dict = Body(...)):
    print()
    return \
        {
        f"message description: {test_result['title']}",
        f"Message Title: {test_result['title']}",
        f"Message Topic-Sub: {test_result['content']}",
        }


#Using BaseModel from pydantic
class Post(BaseModel):
    title: str
    content: str
    closure: str

@app.get("/confirm")
def confirm(template: Post):
    return [
        f"Title: {template.title}",
        f"Content: {template.content}",
        f"Greetings: {template.closure}, Amen!!!",
        f"After implementing my Post class, inheriting the Pydantic Basemodel, "
        f"at first I made a mistake of relating with the Post class as a dictionary "
        f"having passed it like this: 'def confirm(template: Post)'",
        "I had to run {template.title}, {template.content}, and {template.closure} to get a response."
    ]

class KeepTrying(BaseModel):
    status: str
    details: str

@app.post("/with basemodel")
def basemodel(new : dict = Body(...)):
    return \
        [
            f"Status: {new['status']}"
        ]

@app.get("/check")
def check(stat: dict= KeepTrying):
    return [
        "In check",
        stat['status'],
        stat['details'],
        "Syntax: def functionName(parameterName: dict= myClassName): function body",
        "I used the syntax: 'def check(stat: dict= KeepTrying)' to convert the Pydantic Class to a dictionary "
        "and run it like this: stat['status'], stat['details'] to respond with the 'status' value and 'details' value respectively"
    ]

#         THE END OF BASE MODEL PYDANTIC CLASS


@app.get("/what is a crud app")
def crudApp():
    crud_app = (f"CRUD is basically an acronym representing the four main properties of an API",
                f"C -> Create: uses the 'post' path operator",
                "R -> Read: has two 'get' path operators: '.get/posts/{id}' - for retrieving a specific data - "
                "and '.get/posts/ - for retrieving all data.",
                f"U -> Update: uses the 'put' or 'patch' path operator. 'put' path operator changes the entire content of a post, while "
                f"'patch' path operator changes a specific part of the post",
                f"D -> Delete: uses the 'delete' path operator",
                f""
                )
    return crud_app




@app.get("/our urls and descriptions")
def urlsAndDescriptions():
    baseurl = "http://127.0.0.1:8000"
    info = {
        f"{baseurl}/": "Returns how to a create Fast API function and path",
        f"{baseurl}/uvicorn run info": "Returns the different ways of running a uvicorn application through terminal",
        f"{baseurl}/student details": "Displays student information and manipulates it",
        f"{baseurl}/create post": "First 'post' decorator test",
        f"{baseurl}/getting date and time": "Returns date and time of today and now",
        f"{baseurl}/a knowing": "First fastapi.params.Body test",
        f"{baseurl}/testing stuff": "Second fastapi.params.Body test",
        f"{baseurl}/confirm": "First test for Pydantic BaseModel as a Class",
        f"{baseurl}/with basemodel": "First test for Pydantic as a Dictionary",
        f"{baseurl}/check": "Second test for Pydantic BaseModel as a Dictionary",
        f"{baseurl}/our urls and descriptions": "Returns the list of all urls and description",
        f"{baseurl}/what is a crud app": "Explains a CRUD app"
    }
    return \
[
    f"There are {len(info.keys())} items of the list below",
    info
]