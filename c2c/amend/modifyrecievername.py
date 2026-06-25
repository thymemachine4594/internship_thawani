#The application can call the Update Receiver Name endpoint to allow the amend of the Receiver's Name on a transactionId resource. (PATCH)
import requests

url = "https://sandboxapi.moneygram.com/amend/v1/transactions/transactionId/receiver/name?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150519"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.patch(url, headers=headers)

print(response.text)