import asyncio
import json

from web3 import Web3
from web3.exceptions import BadFunctionCallOutput

from app.core.config import settings

WEB3_PROVIDER_URI = settings.WEB3_PROVIDER_URI
CONTRACT_ADDRESS = settings.CONTRACT_ADDRESS
ERC20_ABI = settings.ERC20_ABI

web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
CHECKSUM_ADDRESS = Web3.to_checksum_address(CONTRACT_ADDRESS)


if web3.is_connected():
    print('connected')


token_contract = web3.eth.contract(CHECKSUM_ADDRESS, abi=ERC20_ABI)


async def get_balance(address: str) -> str:
    checksum_address = web3.to_checksum_address(address)
    balance = await asyncio.to_thread(token_contract.functions.balanceOf(checksum_address).call)
    return balance

