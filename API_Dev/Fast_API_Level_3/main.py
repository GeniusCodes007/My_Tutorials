from fastapi import FastAPI
from pydantic_models import (Student, Percent, Customer)

app = FastAPI()

@app.post("/marks", response_model=Percent)
async def get_percent(student: Student):
    student.percent_grade = sum(student.grade)/2
    return student

@app.get("/customer")
async def customer_info(customer: Customer):
    return customer