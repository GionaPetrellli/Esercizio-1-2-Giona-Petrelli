from fastapi import FastAPI, Depends
from Repo.Email_Db import get_db, engine, Base
from Dto.Email_Dto import EmailRequest
from Service.Email_Service import EmailService

app = FastAPI()


Base.metadata.create_all(bind=engine)

service = EmailService()


@app.post("/invia")
async def handle(data: EmailRequest, db=Depends(get_db)):
    return await service.invia(data, db)
