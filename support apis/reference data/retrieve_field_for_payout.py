#Retrieve Fields for a Payout endpoint retrieves all the required, and optional fields, and metadata for a send transaction based a service option, receive amount, and receive currency.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/transaction-fields-receive?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=EN-US&amount=100&receiveCurrencyCode=USD"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)