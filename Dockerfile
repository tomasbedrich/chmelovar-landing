FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

RUN pip install llconfig jinja2 aiofiles email-validator python-multipart sendgrid motor sentry-sdk==0.13.5

COPY ./app /app
