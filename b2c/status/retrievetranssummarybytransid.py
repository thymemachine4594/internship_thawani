#The application can invoke the Retrieve a Transaction endpoint to lookup by transactionId and return the current status of a transaction. (GET)
import requests

url = "https://sandboxapi.moneygram.com/disbursement/status/v1/transactions/lite/transactionId?targetAudience=AGENT_FACING&userLanguage=en-US&agentPartnerId=30150519"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)