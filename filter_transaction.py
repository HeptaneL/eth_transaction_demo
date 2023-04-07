# Import necessary libraries
from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('YOUT INFURA PROJECT API'))

# Define filter parameters
contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7' # Replace with actual contract address
with open("./erc20.abi") as f:
    abi = json.load(f)
from_block = 16997200 # Replace with actual block number
to_block = 'latest'
#topics = ['0xa9059cbb000000000000000000000000' + 'address_to_filter'.rjust(64, '0')] # Replace 'address_to_filter' with actual address
topics = ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef']
# Create filter and get logs
filter_params = {'fromBlock': from_block, 'toBlock': to_block, 'address': contract_address, 'topics': topics}
filter = w3.eth.filter(filter_params)
logs = w3.eth.get_filter_logs(filter.filter_id)
contract = w3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=abi)
# Print logs
for log in logs:
    blockNumber = log.blockNumber
    logIndex = log.logIndex
    transactionHash = log.transactionHash.hex()
    parsed_log = contract.events.Transfer().process_log(log)
    fromAccount = parsed_log["args"]["from"]
    toAccount = parsed_log["args"]["to"]
    value = parsed_log["args"]["value"]/100000
    transaction = f"blockNumber: {blockNumber} logIndex: {logIndex} transactionHash: {transactionHash} from: {fromAccount} to: {toAccount} value: {value}"
    print(transaction)
