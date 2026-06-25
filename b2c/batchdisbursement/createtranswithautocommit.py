#The Create API determines what information to collect from the customer, validates the data for compliance purposes and creates the transactionId resource.(POST)
import requests

url = "https://sandboxapi.moneygram.com/disbursement/v1/transactions"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": 30150519,
    "userLanguage": "en-US",
    "destinationCountryCode": "USA",
    "destinationCountrySubdivisionCode": "US-MN",
    "serviceOptionCode": "WILL_CALL",
    "autoCommit": True,
    "sendAmount": {
        "value": 100,
        "currencyCode": "USD"
    },
    "receiveCurrencyCode": "USD",
    "sender": { "business": {
            "businessType": "ACCOMMODATION_HOTELS",
            "businessIssueDate": "2024-04-29",
            "address": {
                "line2": " ",
                "line3": " ",
                "countrySubdivisionCode": "US-MN",
                "postalCode": 55103
            },
            "contactDetails": {
                "email": "acmecorp@mail.com",
                "phone": {
                    "number": 5551231234,
                    "countryDialCode": 1
                }
            }
        } },
    "beneficiary": { "consumer": {
            "address": {
                "countrySubdivisionCode": "US-MN",
                "postalCode": 55442
            },
            "mobilePhone": {
                "number": 5551231234,
                "countryDialCode": 1
            }
        } }
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)