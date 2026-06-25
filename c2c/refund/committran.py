#The Commit API executes the transactionId and completes the refund.

import requests

url = "https://sandboxapi.moneygram.com/refund/v2/transactions/transactionId/commit"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": 30150519
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)