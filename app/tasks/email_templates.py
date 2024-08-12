from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_verification_template(
    email_to: EmailStr,
    token: str
):
    email = EmailMessage()

    email["Subject"] = "Подтверждение регистрации"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Подтвердите регистрации</h1>
            Ваш код верификации: {token}
        """,
        subtype="html",
    )
    return email
