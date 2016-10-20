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


def getOpener(header):
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    ckjar = cookiejar.CookieJar()
    ckpro = request.HTTPCookieProcessor(ckjar)
    opener = request.build_opener(ckpro)
    headers = []
    for key, value in header.items():
        ele = (key, value)
        headers.append(ele)
    opener.addheaders = headers
    return opener


def getxsrf(data):
    ls = re.findall('name=\"_xsrf\" value=\"(.*)\"', str(data))
    return ls[0]

header = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/49.0.2623.75 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'DNT':'1'
    }

if __name__ == '__main__':
    url = "https://www.zhihu.com"
    req = request.Request(url, headers=header)

    with request.urlopen(url) as res:
        data = res.read()
        data = ungzip(data)
        _xsrf = getxsrf(data.decode('utf-8'))

    opener = getOpener(header)
    url+='login/email'
    eml='***************'
    passwd='*********'

    postdict = {
        '_xsrf':_xsrf,
        'email': eml,
        'password': passwd,
        'remember_me': 'true'
    }

    postdata = parse.urlencode(postdict).encode()
    res = opener.open(url, postdata)
    data = res.read()

    data = ungzip(data)
    print(data.decode())