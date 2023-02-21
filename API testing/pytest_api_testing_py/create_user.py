import requests
import data

url = "https://reqres.in/api/users"
response = requests.post(url, data.payload)
print(response.status_code)
print(response.json())