import requests

response = requests.get("https://reqres.in/api/users?page=2")
data = dict(response.json())
print(data['total'])
print(data['data'][0]["first_name"])

print(response.status_code)