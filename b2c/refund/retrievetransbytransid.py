#The Retrieve a transaction endpoints look-up and returns a transaction by referenceNumber or transactionId for the purpose of refund. (GET)
import requests

url = "https://sandboxapi.moneygram.com/disbursement/refund/v1/transactions/transactionId?targetAudience=AGENT_FACING&userLanguage=en-US&agentPartnerId=30150519&refundReasonCode=INCORRECT_AMT"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)