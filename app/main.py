from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import EmailStr
from config import config

from services import record_subscribe_request, submit_contact_form

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


if config['FORCE_HTTPS']:
    @app.middleware("http")
    async def force_https(request: Request, call_next):
        # fake HTTPS request scope because of following bug:
        # https://github.com/encode/uvicorn/issues/505
        request.scope["scheme"] = "https"
        response = await call_next(request)
        return response


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
