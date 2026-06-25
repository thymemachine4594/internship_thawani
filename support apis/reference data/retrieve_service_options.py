#Retrieves superset of applicable service options to use with MoneyGram API Integrations. This is to provide a reference during development as well as to enable implementors to cache the set of enumerations.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/service-options?targetAudience=AGENT_FACING&userLanguage=EN-US&destinationCountryCode=USA"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)