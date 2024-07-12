from typing import Union

from pydantic import BaseModel


class AddressesRequest(BaseModel):
    address: Union[list[str], str]

