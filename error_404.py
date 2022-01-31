import requests
response = requests.get('http://localhost/blogger1')
print(response.status_code)
#response.raise_for_status()
