#The application can invoke the Update a business profile to make changes to a business profile.(PUT)
import requests

url = "https://sandboxapi.moneygram.com/business/v1/profiles/businessProfileId"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": "30150519",
    "userLanguage": "en-US"
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)