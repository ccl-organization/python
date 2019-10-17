#coding:utf-8
#本实例用于获取糗事百科热门的文章内容和好评数量。
import urllib2
import re
from bs4 import BeautifulSoup
#糗事百科需要设置MIME头才能正常请求，不需要登陆，也不需要cookie
print('=======================糗事百科数据挖掘==========================')

urlstr="https://www.qiushibaike.com/8hr/page/%d"


data={}
def getdata(html):  #从字符串中安装正则表达式获取值
    soup = BeautifulSoup(html, 'html.parser');
    alldiv = soup.find_all("div", class_="content")   #内容的外部div
    allnum = soup.find_all("span", class_="stats-vote")  #点赞数量的外部span
    for i in range(0,len(alldiv)):
        print (str(alldiv[i].find_all('span')[0]).replace('<span>','').replace('</span>','').replace('<br/>','\r\n').strip() )
        #内容文字，使用string在文字里还有<br/>时，无法打印，使用text会省略调用<br/>
        print (allnum[i].find_all('i')[0].string )
        #好评数量





#根据一个网址，获取该网址中符合指定正则表达式的内容
def craw(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }  #设置MIME头，糗事百科对这个进行了验证
        request = urllib2.Request(url,headers = headers)  #创建一个请求
        response = urllib2.urlopen(request)  #获取响应
        html = response.read()  #读取返回html源码
        getdata(html)

    except urllib2.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print (e.reason)


for i in range(1,14):
    url = urlstr % i
    print(url)
    craw(url)
