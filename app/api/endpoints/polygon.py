from typing import Annotated

from fastapi import APIRouter, Body

from app.api.schemas.polygon import BalancePost
from app.utils.polygon import get_balance

polygon_router = APIRouter(
    prefix="",
    tags=["Polygon"]
)


@polygon_router.get('/get_balance/', status_code=200)
async def get_balance(address: str):
    balance = get_balance(address)
    return {'balance': balance}


@polygon_router.post('/get_post/', status_code=200)
async def get_balance(address: BalancePost):
    balances = [get_balance(addr.address) for addr in address]
    return {'balances': balances}
