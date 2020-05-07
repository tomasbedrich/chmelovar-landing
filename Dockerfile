FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8-2020-04-27

RUN pip install llconfig jinja2 aiofiles email-validator python-multipart sendgrid motor sentry-sdk

COPY ./app /app
