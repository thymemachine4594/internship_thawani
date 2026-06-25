#Search for a consumer by MoneyGram Rewards number, phone number, or identification type and number.(GET)
import requests

url = "https://sandboxapi.moneygram.com/consumer/v2/profiles/search?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=en-US&mobilePhone=5551231234&maxProfilesToReturn=20&pageNumber=1&perPage=20"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)