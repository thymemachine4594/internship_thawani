#Creates payout transaction with specific payout option and verifies whether the information collected about the sender is sufficient for identification and regulatory purposes. 
#It returns a unique transaction id that needs to be submitted with subsequent update and commit call. (POST)
import requests

url = "https://sandboxapi.moneygram.com/transfer/v1/transactions"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)