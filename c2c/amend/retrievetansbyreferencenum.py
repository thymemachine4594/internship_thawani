#The application can invoke the Retrieve a Transaction endpoints to lookup by referenceNumber and return a transaction for amend. (GET)
import requests

url = "https://sandboxapi.moneygram.com/amend/v1/transactions?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150519"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)