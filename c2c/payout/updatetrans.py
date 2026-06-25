#The Payout Update API determines what information to collect from the customer, validates the data for compliance purposes and updates the transactionId resource with the data collected. (PUT)
import requests

url = "https://sandboxapi.moneygram.com/payout/v1/transactions/transactionId?targetAudience=AGENT_FACING&userLanguage=EN-US&agentPartnerId=30150535"

payload = { "receiver": {
        "address": {
            "line1": "Lodhi Road",
            "city": "New Delhi",
            "countrySubdivisionCode": "IN-DL",
            "countryCode": "IND",
            "postalCode": 110001
        },
        "mobilePhone": {
            "number": "07311234-5678",
            "countryDialCode": 91
        },
        "personalDetails": {
            "birthCity": "New Delhi",
            "birthCountryCode": "IND",
            "citizenshipCountryCode": "IND"
        },
        "primaryIdentification": {
            "typeCode": "PAS",
            "id": "P12122345",
            "issueCountrySubdivisionCode": "IN-DL",
            "issueCountryCode": "IND",
            "issueCity": "New Delhi"
        },
        "secondaryIdentification": {
            "typeCode": "ALN",
            "id": 565455698,
            "issueCountrySubdivisionCode": "IN-DL",
            "issueCountryCode": "IND",
            "issueCity": "New Delhi"
        }
    } }
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)