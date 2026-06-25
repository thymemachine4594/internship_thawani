#The Payout Commit API executes the transactionId and completes the payout of funds.(PUT)
import requests

url = "https://sandboxapi.moneygram.com/payout/v1/transactions/transactionId/commit?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150535"

payload = { "partnerTransactionId": "5e62c3c3-06da-43bc-86c1-90f5d86a6f90" }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)