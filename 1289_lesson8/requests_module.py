import requests

resp = requests.get("https://github.com/requests")
print(resp)
# print(resp.text)
print(type(resp))
print(resp.status_code)
print(resp.headers)

resp = requests.put("https://github.com/requests/put")
print(resp)
print(resp.text)

resp = requests.delete("https://github.com/requests/delete")
print(resp)
print(resp.text)
print(resp.status_code)
print(resp.headers)

resp = requests.head("https://github.com/requests/get")
print(resp)

# data = {'key': 'value'}
# resp = requests.get("https://github.com/requests/", param=data)


