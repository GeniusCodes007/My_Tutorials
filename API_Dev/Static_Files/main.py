from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

template = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"),
          name="static")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(name: str, request:Request):
    return template.TemplateResponse("logo.html",
                                     {"request": request,
                                      "name": name})