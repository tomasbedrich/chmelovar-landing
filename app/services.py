import logging
from starlette.requests import Request
from pydantic import EmailStr
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From
from motor.motor_asyncio import AsyncIOMotorClient
from config import config


mongo = AsyncIOMotorClient(config['MONGO_CONNECTION_STRING'])
db = mongo['default']


async def record_subscribe_request(http_request: Request, email: EmailStr):
    record = {
        'http_headers': http_request.headers,
        'email': email,
    }
    result = await db.subscribers.insert_one(record)
    logging.info(f'Subscribe request ID "{result.inserted_id}" processed.')


async def submit_contact_form(http_request: Request, email: EmailStr, name: str, message: str):
    # first log to Mongo as an insurance
    record = {
        'http_headers': http_request.headers,
        'from_email': email,
        'from_name': name,
        'message': message,
    }
    result = await db.contact_form_submissions.insert_one(record)

    envelope = Mail(
        from_email=From(email, name),
        to_emails=config['CONTACT_FORM_RECEPIENT'],
        subject=config['CONTACT_FORM_SUBJECT'],
        plain_text_content=message
    )
    try:
        sg = SendGridAPIClient(config['SENDGRID_API_KEY'])
        response = sg.send(envelope)
        print(response)
        logging.info('Contact form submit processed.')
    except Exception as e:
        logging.exception('Contact form submit failed.')
        raise