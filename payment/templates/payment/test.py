import requests

url = "https://khalti.com/api/v2/merchant-transaction/"
payload = {}
headers = {
  "Authorization": "key test_secret_key_61fda43d5daf40718e3f5c89904bff58"
}

response = requests.get(url, payload, headers = headers)
print(response.text)