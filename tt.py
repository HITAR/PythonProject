html = """
 <span class="link_view" title="阅读次数"><a href="/fly_yr/article/details/52643430" title="阅读次数">阅读</a>(84)</span>

"""
import re
from bs4 import BeautifulSoup

#添加一个解析器
soup = BeautifulSoup(html,'html5lib')
#print(soup.title)
#print(soup.title.name)
#print(soup.find('span',"link_view").a.get("title"))
#print(soup.body)

#从文档中找到所有<a>标签的内容
# for link in soup.find_all('a'):
#     print(link.get('href'))


#从文档中找到所有文字内容
#sprint(soup.get_text())

path = r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CIDOpen'

res = path.split("\\", 1)
r = res[0]

str = re.compile('\'')
key = str.sub("",r)

print(key)
print(res[-1])

