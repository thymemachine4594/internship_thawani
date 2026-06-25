#Retrieves enumerated values for fields. The data returned by the endpoint gives you the exact enumerated fields and values to display in the UI for customer selection. If a field is an enumerated data-type, the values returned in this API are the only accepted values for the field.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/enumerations?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=EN-US&consumerCountryCode=USA"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)