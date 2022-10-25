import requests




def info(network, address):
    url = "https://solana-gateway.moralis.io/nft/" + network + "/" + address + "/metadata"
    headers = {
        "accept": "application/json",
        "X-API-Key": "INxVMcsCPtc93kuuNysk6qUCO8Y60IhcLTUi9K4n6IHMjLE3eF0XTzlJtmCZc3yp"
    }
    response = requests.get(url, headers=headers)
    return response
