# -*- coding: UTF-8 -*-

from urllib.parse import urlparse, parse_qs,unquote

str=''
method = '/si  mila r'.replace(' ', '').replace("/", '')
print(method)


if "similar" is method:
    print('ok')
else:
    print('no ')

urldata='word=%E6%A0%BC%E6%A0%BC%E4%B8%8D%E5%85%A5'

urldata = unquote(urldata, encoding='gbk', errors='replace')
res=urlparse(urldata)
print(res)


import urllib.parse
s1='sentences=%E5%8D%A1%E5%A4%AB%E5%8D%A1&id=101'
print(urllib.parse.unquote("%E6%B5%8B%E8%AF%95abc"))
print('s1',urllib.parse.unquote(s1))

ary1='[-1.6975654 - 0.09812085  2.1600244   2.58708     1.3168149 - 2.6738997]'