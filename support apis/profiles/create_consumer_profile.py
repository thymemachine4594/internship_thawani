#The Create a consumer profile api determines the information required to create a new consumer profile.(POST)
import requests

url = "https://sandboxapi.moneygram.com/consumer/v2/profiles"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": 30150519,
    "userLanguage": "en-US"
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)