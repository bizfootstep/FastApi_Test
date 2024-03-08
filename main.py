from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit/", response_class=HTMLResponse)
async def submit_form(request: Request, name: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})
