#Reversal of the transaction if received in error, or if a failure in some other part of the system requires the rollback of a transaction.(PUT)
import requests

url = "https://sandboxapi.moneygram.com/payout/v1/transactions/transactionId/reverse?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150535"

payload = { "receiveReversalReasonCode": "WANTS_CASH" }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)