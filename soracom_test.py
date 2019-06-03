from soracom.client import *
client = SoracomClient()
y = client.auth(email="poc+SrihariS@soracom.jp", password="CixmwAkzZRUbRbywvUJMHY9T")
print("\nAuthentication Response: ", y)
x = client.get("/subscribers")
print ("\nSubscribers info: ",x)
