import requests
try:
    r=requests.get("https://httpbin.org/delay/5", timeout=2)
    print(r.status_code)
except requests.exceptions.ReadTimeout:
    print("time out exception occured!")