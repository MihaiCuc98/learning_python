import requests

params = {'page': 2}

response = requests.get("https://reqres.in/api/users/336", params=params)
print(response.status_code)
json_response = response.json()
print(response.json())
