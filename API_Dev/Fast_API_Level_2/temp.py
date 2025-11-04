from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="templates")


@app.get("/hello/")
async def hello():
    ret = '''
    <html>

<body>
    <h1>Hello!!! Genius Codes </h1>
    <h2>Welcome to the world of Fast API </h2>
    <h3>We heard this was your first output like 
    this!!!</h3>
</body>

</html>
    '''
    return HTMLResponse(content=ret)

@app.get("/hello 2/", response_class=HTMLResponse)
async def hello(request: Request):
    return template.TemplateResponse("hello.html",
                                     {"request": request})

@app.get("/working with parameters/{name}",
         response_class=HTMLResponse)
async def hello(name:str, request:Request):
    return template.TemplateResponse("parameter.html",
                                     {"request": request,
                                      "name": name})