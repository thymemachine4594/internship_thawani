#The FX API returns the the estimated fx rates for the service options available in a destination country.(GET)
import requests

url = "https://sandboxapi.moneygram.com/fx-rate/v1/rates?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150519&originatingCountryCode=USA&destinationCountryCode=IND&sendCurrencyCode=USD"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)