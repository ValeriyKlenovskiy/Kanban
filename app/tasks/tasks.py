import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.tasks.celeryfile import celery
from app.tasks.email_templates import create_verification_template


@celery.task
def process_pic(path: str):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_1000_500 = im.resize((1000, 500))
    im_resized_200_100 = im.resize((200, 100))
    im_resized_1000_500.save(f"app/static/images/b_{im_path.name}")
    im_resized_200_100.save(f"app/static/images/s_{im_path.name}")


@celery.task
def send_verification_email(
    email_to: EmailStr,
    token: str
):
    # Удалите строчку ниже для отправки сообщения на свой email, а на пользовательский
    email_to = settings.SMTP_USER
    msg_content = create_verification_template(email_to, token)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
    print(f"Successfully send email message to {email_to}")


'''
celery --app=app.tasks.celeryfile:celery worker -l INFO
celery --app=app.tasks.celeryfile:celery flower --url_prefix=/flower

'''