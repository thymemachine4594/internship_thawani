#Commit a Transaction (PUT)
#The Commit API executes the transactionId and completes the transfer of funds.

url = "https://sandboxapi.moneygram.com/disbursement/v1/transactions/quote"

headers = {
    "accept": "application/json",
    "X-MG-ClientRequestId": "4c79b06f-a2af-4859-82c8-28cbb0bf361b",
    "content-type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)