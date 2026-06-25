#The application can invoke the Retrieve a Transaction API to look-up and return a transaction for payout.(GET)
import requests

url = "https://sandboxapi.moneygram.com/payout/v1/transactions?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150535"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)