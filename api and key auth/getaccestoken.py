#Get Access Token (GET)
#api get response
import requests

url = "https://sandboxapi.moneygram.com/oauth/accesstoken?grant_type=client_credentials"

headers = {
    "accept": "application/json",
    "authorization": "Basic bmliek5oNHR1bXk1ZmZMc3pIYjVPcUtSQVRtcVZLazI6dHZPS1h6eFg4RUNUM05VbQ"
}

response = requests.get(url, headers=headers)

print(response.text)
