#Commit a Transaction (POST)
#The Commit API executes the trasnsactionId and completes the transfer of funds.
import requests

url = "https://sandboxapi.moneygram.com/transfer/v1/transactions/transactionId/commit"

payload = { "partnerTransactionId": "75370815-016e-410c-8acf-7056731231b4" }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)