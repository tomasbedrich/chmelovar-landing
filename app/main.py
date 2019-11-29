from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import EmailStr

from services import record_subscribe_request, submit_contact_form

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/subscribe")
async def subscribe(http_request: Request, email: EmailStr = Form(...)):
    await record_subscribe_request(http_request, email)
    return True


@app.post("/contact")
async def contact(http_request: Request, email: EmailStr = Form(...), name: str = Form(...), message: str = Form(...)):
    await submit_contact_form(http_request, email, name, message)
    return True