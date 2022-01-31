from urllib.request import Request,urlopen
req = Request('http://localhost/blogger',method='HEAD')
response = urlopen(req)
print(response.status)
print(response.read())
