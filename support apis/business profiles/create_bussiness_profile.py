#The create business profile API creates a new business profile.(POST)
import requests

url = "https://sandboxapi.moneygram.com/business/v1/profiles"

payload = {
    "targetAudience": "AGENT_FACING",
    "agentPartnerId": "30150519",
    "userLanguage": "en-US",
    "businessDetails": {
        "address": {
            "countrySubdivisionCode": "US-TX",
            "postalCode": "75001"
        },
        "contactDetails": {
            "email": "business@mail.com",
            "phone": {
                "number": "5551231234",
                "countryDialCode": "1"
            }
        }
    }
}
headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
