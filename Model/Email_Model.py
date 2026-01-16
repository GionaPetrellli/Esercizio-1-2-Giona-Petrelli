from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from Repo.Email_Db import Base


class EmailLog(Base):
    __tablename__ = "sendmails"

    id = Column(Integer, primary_key=True)
    emailDestinatario = Column(String)
    emailtype = Column(String)
    data_invio = Column(DateTime(timezone=True), server_default=func.now())
