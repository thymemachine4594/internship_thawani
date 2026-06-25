#Account deposit fields.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/account-deposit-fields?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=EN-US&destinationCountryCode=USA"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)