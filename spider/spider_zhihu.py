from urllib import request
from urllib import parse
from http import cookiejar
import re
import gzip


def ungzip(data):
    try:
        print("decompress...")
        data = gzip.decompress(data)
        print("decompress finished.")
    except:
        print("no need to decompress")
    return data

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
def getopener(header):
    #声明一个cookiejar对象来保存cookie
    ckjar = cookiejar.CookieJar()
    #创建cookie处理器
    ckpro = request.HTTPCookieProcessor(ckjar)
    #创建opener
    opener = request.build_opener(ckpro)

    headers = []
    for key, value in header.items():
        ele = (key, value)
        #print(ele)
        headers.append(ele)
    opener.addheaders = headers
    return opener


def getxsrf(data):
    #cer = re.compile('name=\"_xsrf\" value=\"(.*)\"',flags=0)
    #strlist = cer.findall(data)
    list = re.findall(r'name="_xsrf" value="*"', str(data))
   # print(list)
    return list[0]

headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/49.0.2623.75 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

if __name__ == '__main__':
    url = "https://www.zhihu.com"
    req = request.Request(url, headers=headers)

    with request.urlopen(req) as res:
        data = res.read()
        data = ungzip(data)
        _xsrf = getxsrf(data.decode('utf-8'))
    #print(1)

    opener = getopener(headers)
    url+='/login/email'
    eml='*'
    passwd='*'

    postdict = {
        '_xsrf':_xsrf,
        'email': eml,
        'password': passwd,
        'remember_me': 'true'
    }

    #要post的数据
    postdata = parse.urlencode(postdict).encode()
    #print(postdata)

    #模拟登陆
    res = opener.open(url, postdata)
    #print(2)
    data = res.read()
    data = ungzip(data)
    print(data.decode())