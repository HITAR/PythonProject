from urllib import request

#请求

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}

req = request.Request(url, headers=header)
#req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')

#爬取结果

with request.urlopen(req) as f:
    data = f.read()
    print("Status:", f.status, f.reason)
   # for i, j in f.getheaders():
   #     print("%s %s" %(i, j))
   # print(f.info())
    print('Data:', data.decode('utf-8'))
'''

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

'''