#The application can invoke the delete a business profile to delete a business profile.(DELETE)
import requests

url = "https://sandboxapi.moneygram.com/business/v1/profiles/businessProfileId?targetAudience=AGENT_FACING&userLanguage=en-US&agentPartnerId=30150519"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.delete(url, headers=headers)

print(response.text)