import asyncio
from web3 import Web3
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



async def get_all_transfer_events():
    try:
        transfer_filter = await asyncio.to_thread(token_contract.events.Transfer.createFilter, {'fromBlock': 0})
        events = await asyncio.to_thread(transfer_filter.get_all_entries)
        return events
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_top_holders(events, top_n):
    balances = {}
    for event in events:
        from_address = event['args']['from']
        to_address = event['args']['to']
        value = event['args']['value']
        if from_address != '0x0000000000000000000000000000000000000000':
            balances[from_address] = balances.get(from_address, 0) - value
        balances[to_address] = balances.get(to_address, 0) + value

    top_holders = sorted(balances.items(), key=lambda item: item[1], reverse=True)[:top_n]
    return top_holders

