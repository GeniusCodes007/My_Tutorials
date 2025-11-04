from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic_models import User

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def greet(name: str, request: Request):
    return template.TemplateResponse("hello.html",
                                     {"request": request,
                                      "name": name})

@app.get("/login", response_class=HTMLResponse)
async def login(request:Request):
    return template.TemplateResponse("login.html",
                                     {"request": request})

user = "Genius"
passw_ = "12nm"
pin = 2088

@app.post("/submit")
async def submit(nm: str=Form(...), pwd: str=Form(...)):
    if nm == user and pwd == passw_:
        return f"Welcome Back {nm}"
    return "Check Your Inputs"
