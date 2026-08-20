import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://api.github.com", params=payload)

print(r.status_code)
print(r.json(),type(r.json()))