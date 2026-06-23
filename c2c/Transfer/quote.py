#Quote a transaction (PUT)
#The Quote API creates a transactionId resource and determines the service options, currencies and pricing available to a destination country.
import requests

url = "https://sandboxapi.moneygram.com/transfer/v1/transactions/quote"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": 30150519,
    "destinationCountryCode": "IND",
    "serviceOptionCode": "WILL_CALL",
    "sendAmount": {
        "value": 100,
        "currencyCode": "USD"
    }
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

