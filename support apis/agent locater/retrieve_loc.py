#Returns all locations within the specified search radius(GET)
import requests

url = "https://sandboxapi.moneygram.com/agentlocator/v2/locations?address=2990%20N%20Houston%20St%2075201&country=US&searchRadius=5"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)