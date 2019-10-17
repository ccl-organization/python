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


def  getcontentCorpos(path):
    filePaths = []
    fileContents = []
    for root, dirs, files in os.walk( path):
        for name in files:
            filePath = os.path.join(root, name)
            filePaths.append(filePath)
            f = codecs.open(filePath, 'r', 'utf-8')  # 1.文件路径 2.打开方式 3.文件编码
            fileContent = f.read()
            f.close()
            fileContents.append(fileContent)
    corpos = pandas.DataFrame({
        'filePath': filePaths,
        'fileContent': fileContents
    })  # type: DataFrame
    return corpos

def getSegment(corpos):
    segments = []
    filePaths = []
    for index, row in corpos.iterrows():
        filePath = row['filePath']
        fileContent = row['fileContent']
        segs = jieba.cut(fileContent)
        for seg in segs:
            segments.append(seg)
            filePaths.append(filePath)

    segmentDataFrame = pandas.DataFrame({
        'segment': segments,
        'filePath': filePaths
    })
    return segmentDataFrame

def getWordcount(segmentDataFrame):
    # 进行词频统计
    segStat = segmentDataFrame.groupby(  # 调用groupby方法
        by="segment"
    )["segment"].agg({
        "计数": numpy.size
    }).reset_index().sort_values(  # 重新设置索引
        by=['计数'],
        ascending=False  # 倒序排序
    )
    """排在前面的为停用词"""
    # print segStat
    return segStat

def stopword(path_stopword,segStat):
    # 移除停用词
    stopwords = pandas.read_csv(
       path_stopword,
        encoding='utf8',
        index_col=False
    )
    # 获得没有停用词的词频统计结果
    fSegStat = segStat[
        ~segStat.segment.isin(stopwords.stopword)
    ]  # '~'取反，不包含停用词的留下。
    print fSegStat
    return fSegStat


path="/Users/chenyahui/python_data/daoshangshudian"
path_feature_word="/Users/chenyahui/dook_python/data/featureWord.txt"
path_stopword="/Users/chenyahui/dook_python/data/stopWord.csv"

corpos=getcontentCorpos(path)
segment=getSegment(corpos)
segStat=getWordcount(segment)
stopword_segstat=stopword(path_stopword,segStat)




print
jieba.add_word('on')#添加词库
jieba.load_userdict(path_feature_word)
for w in jieba.cut("我爱Python abcde fgh"):
    print(w)
print