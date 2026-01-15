from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Dto.Email_Dto import EmailRequest
from Service.Email_Service import Email_Service
from Repo.Email_Db import db as SessionLocal, engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
email_Service = Email_Service()


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.post("/api/internal/emails/send/v1")
def inviaEmail(richiesta: EmailRequest, db: Session = Depends(get_db)):
    risultato = email_Service.mandaEmail(richiesta, db)
    return risultato
