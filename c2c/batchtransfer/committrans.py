#The Commit API executes the trasnsactionId and completes the transfer of funds. (PUT)
import requests

url = "https://sandboxapi.moneygram.com/transfer/v1/transactions/transactionId/commit"

payload = { "partnerTransactionId": "3b4657cb-9cb7-467c-8bb1-64952d5244c3" }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)