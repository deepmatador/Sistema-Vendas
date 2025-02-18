from pydantic import BaseModel


class LoginData(BaseModel):
    User: str
    Password: str