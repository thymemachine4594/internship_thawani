#Retrieve Fields for a Transfer endpoint retrieves all the required, and optional fields, and metadata for a send transaction based a service option, destination country, send amount, and send and receive currency.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/transaction-fields-send?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=EN-US&destinationCountryCode=USA&serviceOptionCode=WILL_CALL&amount=100&sendCurrencyCode=USD&receiveCurrencyCode=USD"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)