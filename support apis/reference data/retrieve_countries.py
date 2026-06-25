#Retrieves supported values and metadata for all countries. The data returned by the endpoint provided accepted sendCurrencies, receiveCurrencies, phoneDialCodes and accepted values.(GET)
import requests

url = "https://sandboxapi.moneygram.com/reference-data/v1/countries?targetAudience=AGENT_FACING&userLanguage=EN-US"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b"
}

response = requests.get(url, headers=headers)

print(response.text)