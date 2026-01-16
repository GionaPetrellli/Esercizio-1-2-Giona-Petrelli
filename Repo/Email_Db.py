from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi_mail import ConnectionConfig

URL = "postgresql://postgres:Its2025!@localhost/sendmails"
engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

conf = ConnectionConfig(
    MAIL_USERNAME="215e339701bb27",
    MAIL_PASSWORD="b1bb0f7c163cfb",
    MAIL_FROM="qualcuno@gmail.com",
    MAIL_PORT=2525,
    MAIL_SERVER="sandbox.smtp.mailtrap.io",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class EmailRepository:
    def save_log(self, db, fields):
        from Model.Email_Model import EmailLog

        nuovo_log = EmailLog(**fields)
        db.add(nuovo_log)
        db.commit()
        db.refresh(nuovo_log)
        return nuovo_log
