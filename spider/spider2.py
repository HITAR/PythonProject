from urllib import request
import os
import re

target_path = "E:\photos5"
def savefile(path):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    pos = path.rindex('/')
# 字符串拼接
    photo = os.path.join(target_path, path[pos+1:])
    return photo


if __name__ == '__main__':
    url = "https://www.douban.com"

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/49.0.2623.75 Safari/537.36'}
    req = request.Request(url, headers=header)

    with request.urlopen(req) as res:
        data = res.read()
    s = set(re.findall(r'(https:[\S]*?(jpg|png|gif))', str(data)))  #re.findall()返回一个list
    print(s)
    for link, t in s:
        print(link)
        try:
            request.urlretrieve(link, savefile(link))
        except:
            print('error')
