import requests
   
headers = {'content-type': 'application/json'}

email = 'poc+SrihariS@soracom.jp'
password = 'CixmwAkzZRUbRbywvUJMHY9T'
payload = {'email': email, 'password": password}
url = 'https://g.api.soracom.io/v1/auth"

data = {'email': email, 'password': password}

r = requests.post(url, data=json.dumps(data))
print(r)
