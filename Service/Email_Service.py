from Dto.Email_Dto import EmailRequest
from Model.Email_Model import Dati
from sqlalchemy.orm import Session


class Email_Service:
    def mandaEmail(self, richiesta: EmailRequest, db: Session):
        if richiesta.emailType == "RESERVE":
            messaggio = f"Conferma Prenotazione per il libro: {richiesta.titoloLibro}"
        else:
            richiesta.emailType == "RETURN"
        messaggio = f" Restituzione libro: {richiesta.titoloLibro}"

        nuovo_record = Dati(
            emailDestinatario=richiesta.emailDestinatario,
            emailType=richiesta.emailType,
            titoloLibro=richiesta.titoloLibro,
            dataInvio=richiesta.dataInvio,
        )

        db.add(nuovo_record)
        db.commit()
        db.refresh(nuovo_record)

        return {
            "status": "success",
            "message": messaggio,
            "id_database": nuovo_record.id,
        }
