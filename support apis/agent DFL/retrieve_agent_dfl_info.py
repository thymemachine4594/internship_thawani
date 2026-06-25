#Retrieves Daily Financial Limit (DFL) information for an agent including main office and POS-level limits(PUT).
import requests

url = "https://extapi.moneygram.com/agent/v1/agentDFL"

payload = { "baseCurrency": "USD" }
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)