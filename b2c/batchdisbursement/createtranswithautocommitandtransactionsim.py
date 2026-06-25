#The Create API determines what information to collect from the customer, validates the data for compliance purposes and creates the transactionId resource.(POST)
import requests

url = "https://sandboxapi.moneygram.com/disbursement/v1/transactions/async"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)