from pydantic import BaseModel


class BalancePost(BaseModel):
    address: str

