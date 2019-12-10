from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from pydantic import EmailStr

import sentry_sdk

from config import config
from services import record_subscribe_request, submit_contact_form

# basics
app_cnf = {
    "title": "Chmelovar",
    "version": "1.0.0",
}

# disable docs
if config["DISABLE_DOCS"]:
    app_cnf["redoc_url"] = None
    app_cnf["docs_url"] = None

# APP
app = FastAPI(**app_cnf)

# static files + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# HTTPS on production
if config['FORCE_HTTPS']:
    @app.middleware("http")
    async def force_https(request: Request, call_next):
        # fake HTTPS request scope because of following bug:
        # https://github.com/encode/uvicorn/issues/505
        request.scope["scheme"] = "https"
        response = await call_next(request)
        return response


@app.on_event("startup")
async def register_sentry():
    sentry_sdk.init(**config.get_namespace("SENTRY_"))


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


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
