from sqlalchemy import Column, Integer, String
from Repo.Email_Db import Base


class Dati(Base):
    __tablename__ = "email_logs"
    id = Column(Integer, primary_key=True, index=True)

    emailDestinatario = Column(String)
    emailType = Column(String)
    titoloLibro = Column(String)
    dataInvio = Column(String)
    nomeUtente = Column(String)
