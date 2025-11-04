from fastapi import FastAPI, Path, Body
from pydantic_models import BooksAndAuthor, Student

app = FastAPI()

"""
pip3 install aiofiles
"""

@app.get("/")
async def home_page():
    return "Our Home Page"

@app.get("/last page/{page_no}")
async def last_page(page_no: int):
    return f"Page {page_no}"

@app.get("/parameter validation/{string}/{integer}/"
         "{floating}")
async def parameter_validation(
        string: str=Path(..., min_length=3, max_length=100),
        integer:int=Path(..., ge=5, le=1000),
        floating: float=Path(..., ge=2, lt=900)):
    return (f"String: {string}, Integer: {integer}, "
            f"Floating Point: {floating}")

my_records = []

@app.post("/post")
async def post(my_post: BooksAndAuthor):
    new_record = my_post.model_dump()
    new_record['id'] = len(my_records) + 1
    new_record['fullName'] = \
        f"{new_record['surname']} {new_record['firstName']}"
    my_records.append(new_record)
    return my_records

@app.post("/students")
async def student_data(name:str=Body(...), age:int= Body(...)):
    return f"Name: {name}, Age: {age}"

@app.post("/student info/{college}")
async def combining_path_and_query_parameters_with_request_body(
        college:str, age:int, student:Student):
    return (f"{student.name}, aged {age} years,"
            f" graduated from {college}")
