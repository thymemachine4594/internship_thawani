#The application can invoke the retrieve consumer transaction history and return an array of a consumer's transaction history by profileId."(GET)
import requests

url = "https://sandboxapi.moneygram.com/consumer/v2/profiles/profileId/transactions?targetAudience=AGENT_FACING&userLanguage=en-US&agentPartnerId=30150519&pageNumber=1&perPage=1"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)