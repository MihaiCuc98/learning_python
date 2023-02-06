import requests
import data

response = requests.put("https://reqres.in/api/users/2", json=data.payload)
print(response.status_code)
print(response.json())
