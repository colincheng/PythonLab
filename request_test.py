import requests

res = requests.get("http://api.open-notify.org/astros.json")
print(res.text)