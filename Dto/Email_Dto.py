from pydantic import BaseModel


class EmailRequest(BaseModel):
    emailDestinatario: str
    emailtype: str = "non_inviata"

    def fields(self):
        return {
            "emailDestinatario": self.emailDestinatario,
            "emailtype": self.emailtype,
        }
