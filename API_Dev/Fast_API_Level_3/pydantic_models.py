from pydantic import BaseModel, Field
from typing import List, Tuple

class Student(BaseModel):
    name: str = Field(None, title="student name",
                      max_length=40)
    grade: List[float]= Field(max_length=7, min_length=4)
    percent_grade: float

class Percent(BaseModel):
    name: str = Field(None, title="student name",
                      max_length=40)
    percent_grade: float

class Supplier(BaseModel):
    supplierID: str= "Sup 1"
    supplierName: str= "Supplier One"

class Product(BaseModel):
    productID: str= "Prod 1"
    productName: str= "Product One"
    price: int = 12
    supp: Supplier = Supplier()

class Customer(BaseModel):
    custID: str= "Cust 1"
    custName: str = "Customer One"
    prod:Product= Product()