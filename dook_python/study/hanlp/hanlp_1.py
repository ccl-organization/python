# # -*- coding: UTF-8 -*-
#
# from pyhanlp import *
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# print sys.getdefaultencoding()
# # 文本推荐
# Suggester = JClass("com.hankcs.hanlp.suggest.Suggester")
# suggester = Suggester()
# title_array = [
#     "威廉王子发表演说 呼吁保护野生动物",
#     "魅惑天后许佳慧不爱“预谋” 独唱《许某某》",
#     "《时代》年度人物最终入围名单出炉 普京马云入选",
#     "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散",
#     "日本保密法将正式生效 日媒指其损害国民知情权",
#     "英报告说空气污染带来“公共健康危机”"
# ]
# for title in title_array:
#     suggester.addSentence(title)
#
# print 'start'
# print(suggester.suggest("陈述", 2))      # 语义
# print(suggester.suggest("危机公关", 1))  # 字符
# print(suggester.suggest("mayun", 1))   # 拼音
# print(suggester.suggest("徐家汇", 1)) # 拼音
# print 'end'
# # 同义改写
# CoreSynonymDictionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")
# text = "这个方法可以利用同义词词典将一段文本改写成意思相似的另一段文本，而且差不多符合语法"
# #print(CoreSynonymDictionary.rewrite(text),'\n')
#
# print "获取同义词 ",CoreSynonymDictionary.rewrite("丢失").encode('utf-8')
# print "获取同义词，不分词，相当于同义改写",CoreSynonymDictionary.rewriteQuickly("丢失信息")
# print "计算文档语义距离",CoreSynonymDictionary.similarity("你好啊","还行吧")
# print "获取词典中的位置",CoreSynonymDictionary.get("丢失")
# print 'end2'
#
