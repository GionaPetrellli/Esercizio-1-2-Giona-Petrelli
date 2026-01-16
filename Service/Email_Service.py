from fastapi_mail import FastMail, MessageSchema, MessageType
from Repo.Email_Db import EmailRepository, conf


class EmailService:
    def __init__(self):
        self.repo = EmailRepository()

    async def invia(self, data, db):
        try:

            message = MessageSchema(
                subject="Test funzionamento",
                recipients=[data.emailDestinatario],
                body="Email di prova, se ti arriva sei il prescelto",
                subtype=MessageType.plain,
            )

            invioMail = FastMail(conf)
            await invioMail.send_message(message)
            data.emailtype = "inviata"
        except Exception as errore:
            print(f"Errore mail: {errore}")
            data.emailtype = "non inviata"

        return self.repo.save_log(db, data.fields())
