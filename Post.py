from urllib.request import Request,urlopen
from urllib.parse import urlencode
data_dict={'p':'python'}
data = urlencode(data_dict).encode('utf-8')
req = Request('http://localhost/blogger', data= data)
req.add_header('content-type','application/x-www-form-urlencode,charset=UTF-8')
req = Request.post('http://localhost/blogger', data= data)
response=urlopen(req)
print(response)
print(response.getheaders)
