import requests
response=requests.get('http://localhost/blogger')
print(response.status_code)
print(response.reason)
print(response.url)
print(response.ok)
print(response.is_redirect)
print(response.text)
print(response.cookies)
#data = {'p','python'}
#response=requests.post('http://localhost/blogger',data=data)
#print(response)
