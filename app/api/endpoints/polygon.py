from typing import Annotated

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from app.api.schemas.polygon import AddressesRequest
from app.utils.polygon import get_balance

polygon_router = APIRouter(
    prefix="",
    tags=["Polygon"]
)


@polygon_router.get('/get_balance/')
async def get_balance_route(address: str) -> JSONResponse:
    try:
        balance = await get_balance(address)
        return JSONResponse({'balance': balance}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@polygon_router.post('/get_balance_batch/')
async def get_balance_batch(address: AddressesRequest) -> JSONResponse:
    try:
        balance = [await get_balance(addr) for addr in address.address]
        return JSONResponse({'balances': balance}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
