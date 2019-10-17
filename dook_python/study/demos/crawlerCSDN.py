#coding:utf-8
#本实例用于获取指定用户csdn的文章名称、连接、阅读数目
import urllib2
import re
from bs4 import BeautifulSoup
#csdn不需要登陆，也不需要cookie,也不需要设置header
print('=======================csdn数据挖掘==========================')
urlstr="http://blog.csdn.net/luanpeng825485697?viewmode=contents"
host = "http://blog.csdn.net/luanpeng825485697"  #根目录

alllink=[urlstr]   #所有需要遍历的网址
data={}
def getdata(html,reg):  #从字符串中安装正则表达式获取值
    pattern = re.compile(reg)
    items = re.findall(pattern, html)
    for item in items:
        urlpath = urllib2.urlparse.urljoin(urlstr,item[0])   #将相对地址，转化为绝对地址
        if not hasattr(object, urlpath):
            data[urlpath] = item
            print urlpath,'     ',  #print最后有个逗号，表示输出不换行
            print item[2], '     ',
            print item[1]



#根据一个网址获取相关连接并添加到集合中
def getlink(url,html):
    soup = BeautifulSoup(html,'html.parser')   #使用html5lib解析，所以需要提前安装好html5lib包
    for tag in soup.find_all('a'):   #从文档中找到所有<a>标签的内容
        link = tag.get('href')
        newurl = urllib2.urlparse.urljoin(url, link) #在指定网址中的连接的绝对连接
        if host not in newurl:  # 如果是站外连接，则放弃
            continue
        if newurl in alllink:   #不添加已经存在的网址
            continue
        if not "http://blog.csdn.net/luanpeng825485697/article/list" in newurl:  #自定义添加一些链接限制
            continue
        alllink.append(newurl)   #将地址添加到链接集合中


#根据一个网址，获取该网址中符合指定正则表达式的内容
def craw(url):
    try:
        request = urllib2.Request(url)  #创建一个请求
        response = urllib2.urlopen(request)  #获取响应
        html = response.read()  #读取返回html源码
        # reg = r'"link_title"><a href="(.*?)">\r\n(.*?)\n.*?</a>'  #只匹配文章地址和名称
        reg = r'"link_title"><a href="(.*?)">\r\n        (.*?)            \r\n.*?</a>[\s\S]*?阅读</a>\((.*?)\)</span>'  # 匹配地址、名称、阅读数目
        getdata(html,reg)
        getlink(url,html)

    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

for url in alllink:
    craw(url)