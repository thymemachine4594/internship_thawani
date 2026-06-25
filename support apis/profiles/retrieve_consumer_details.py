#The Retrieve a Consumer Profile API returns a consumer's profile by profileId. Optionally, it can respond with all the receivers for the consumer and the last transaction sent to each receiver.(GET)
import requests

url = "https://sandboxapi.moneygram.com/consumer/v2/profiles/afe6218c-8958-4c2b-8209-16aa6225c65e?targetAudience=AGENT_FACING&agentPartnerId=30150519&userLanguage=en-US&returnReceivers=true"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)