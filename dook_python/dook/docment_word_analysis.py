# -*- coding: UTF-8 -*-
import os
import os.path
import codecs  # 编码转换
import jieba
import pandas
from pandas import DataFrame
import numpy
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# 全模式
segments = []
seg_list=jieba.cut("他来到了上海交通大学",cut_all=True)
print("【全模式】：" + "/ ".join(seg_list))

path_manchangdegaobie='/Users/chenyahui/python_data/comments/manchangdegaobie.txt'
f = codecs.open(path_manchangdegaobie, 'r', 'utf-8')  # 1.文件路径 2.打开方式 3.文件编码
fileContent = f.read()
f.close()

for x, w in anls.extract_tags(fileContent, topK=100, withWeight=True,allowPOS=('al')):
    print(' 形容词性惯用语  %s %s' % (x, w))

for x, w in anls.extract_tags(fileContent, topK=100, withWeight=True,allowPOS=('bl')):
    print(' 区别词性惯用语  %s %s' % (x, w))

for x, w in anls.extract_tags(fileContent, topK=100, withWeight=True,allowPOS=('z')):
    print(' 状态词  %s %s' % (x, w))

for x, w in anls.extract_tags(fileContent, topK=100, withWeight=True,allowPOS=('xx')):
    print(' 字符串  %s %s' % (x, w))



for x, w in anls.textrank(fileContent, topK=100, withWeight=True,allowPOS=('al')):
    print(' 形容词性惯用语  %s %s' % (x, w))

for x, w in anls.textrank(fileContent, topK=100, withWeight=True,allowPOS=('bl')):
    print(' 区别词性惯用语  %s %s' % (x, w))

for x, w in anls.textrank(fileContent, topK=100, withWeight=True,allowPOS=('z')):
    print(' 状态词  %s %s' % (x, w))

for x, w in anls.textrank(fileContent, topK=100, withWeight=True,allowPOS=('xx')):
    print(' 字符串  %s %s' % (x, w))


print