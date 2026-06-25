#The application can call the Modify Receive Additional Information endpoint to amend the transactionId resource with additional information about the receiver. (PATCH)
import requests

url = "https://sandboxapi.moneygram.com/amend/v1/transactions/transactionId/receiver/additional-data?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150519"

payload = { "receiver": { "personalDetails": { "genderCode": "MALE" } } }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)