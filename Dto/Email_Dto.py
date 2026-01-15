from pydantic import BaseModel


class EmailRequest(BaseModel):
    emailDestinatario: str
    nomeUtente: str
    emailType: str
    titoloLibro: str
    dataInvio: str
