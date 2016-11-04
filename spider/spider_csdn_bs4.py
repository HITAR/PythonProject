'''
program: csdn博客爬虫
function: 用bs4，实现对csdn主页所有博文的日期、主题、访问量、评论个数信息爬取
version: python 3.5.2
time: 2016/11/04
copyright: ar
'''

from urllib import request
from bs4 import BeautifulSoup
import os
import re
import gzip


target_path = "E:\papers2"
def savefile(data,i):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    path = "paper_"+str(i+1)+".txt"
    path = os.path.join(target_path, path)
    file = open(path,'wb')
    page = '当前页：'+str(i+1)+'\n'
    file.write(page.encode(encoding='gb18030'))
    #将博文信息写入文件(以utf-8保存的文件声明为gbk)
    for d in data:
        d = str(d)+'\n'
        file.write(d.encode(encoding='gb18030'))
    file.close()

def ungzip(data):
    try:
    #    print("decompress...")
        data = gzip.decompress(data)
    #    print("decompress finished.")
    except:
        print("no need to decompress")
    return data


class CSDNSpider:
    def __init__(self,pageidx=1,url="http://blog.csdn.net/fly_yr/article/list/1"):
        self.pageidx = pageidx
       # self.url = url[0:url.rindex('/')+1]+str(pageidx)
        self.url = url[0:url.rfind('/') + 1] + str(pageidx)
        # print(self.url)
        self.headers = {
            'Host': 'blog.csdn.net',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/49.0.2623.75 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    def getpage(self):
        req = request.Request(url=self.url, headers=self.headers)
        with request.urlopen(req) as res:
            data = res.read()
            data = ungzip(data)
        data = data.decode('utf-8','ignore')
        soup = BeautifulSoup(data,'html5lib')
        tag = soup.find('div', "pagelist")
        pagedata = tag.span.get_text()
        print(pagedata)
        pagenum = re.findall(re.compile(pattern=r'共(.*?)页'),pagedata)[0]

        #pages = r'<div.*?pagelist">.*?<span>.*?共(.*)?页</span>'
        # pattern = re.compile(pages, re.DOTALL)
        # pagenum = re.findall(pattern, str(data))[0]
        return pagenum

    def setpage(self,idx):
        self.url = self.url[0:self.url.rindex('/')+1]+str(idx)
        #self.url = self.url[0:self.url.rfind('/')+1]+str(idx+1)
        # print(self.url)

    def readdata(self):
        ret = []
        # strs = r'<span.*?link_title"><a href="(.*?)">' +\
        #     r'(.*?)</a></span>' +\
        #     r'.*?<span.*?link_postdate">(.*?)</span>' +\
        #     r'.*?<span.*?link_view".*?>阅读</a>\((.*?)\)</span>' +\
        #     r'.*?<span.*?link_comments".*?>评论</a>\((.*?)\)</span>'
        req = request.Request(url=self.url,headers=self.headers)
        with request.urlopen(req) as res:
            data = res.read()
            data = ungzip(data)
            data = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(data,"html5lib")
        items = soup.find_all('div',"list_item article_item")
        for item in items:

            title = item.find('span',"link_title").a.get_text()
            res = re.split(r'\s+',title)
            res = ''.join(str(e) for e in res)

            link = item.find('span',"link_title").a.get('href')
            date = item.find('span',"link_postdate").get_text()
            view = re.findall(re.compile(r'.*?\((.*?)\)'),item.find('span',"link_view").get_text())[0]
            comments = re.findall(re.compile(r'.*?\((.*?)\)'),item.find('span',"link_comments").get_text())[0]
        # pattern = re.compile(strs, re.DOTALL)
        # items = re.findall(pattern, str(data))
            ret.append('\n标题:'+res+'\t链接：http://blog.csdn.net'+link
                       +'\n发表日期：'+date
                       +'\n阅读：'+view+'\t评论：'+comments+'\n')

        return ret



cs = CSDNSpider()
pages = int(cs.getpage())
print("博文总页数:%d" % pages)
for idx in range(pages):
     cs.setpage(idx)
     print("当前页：%d" % (idx+1))
     #读取当前页的所有博文，结果为list类型
     papers = cs.readdata()
     savefile(papers,idx)