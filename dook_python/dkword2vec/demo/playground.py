# -*- coding: UTF-8 -*-

import tensorflow as tf
# from pypinyin import pinyin, Style
import numpy as np
# from src.common.Kit import RNN
# from src.common.ChineseTextSource import ChineseTextSource
import jieba
from gensim.models import Word2Vec, word2vec
from collections import Counter
import pandas as pd
import csv
import json
import jieba.analyse


# ############################above is the common pare for playground#############

def sort_by_value(input_dict, desc=True):
    items = input_dict.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort(reverse=desc)
    return [backitems[i][1] for i in range(0, len(backitems))], [backitems[i][0] for i in range(0, len(backitems))]


def predict_proba(model, oword, iword):
    # 获取输入词的词向量
    iword_vec = model[iword]
    # 获取保存权重的词的词库
    oword = model.wv.vocab[oword]
    oword_l = model.trainables.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code * dot)
    return lprob


def keywords(model, sentences):
    # 抽出s中和与训练的model重叠的词
    sentences = [word for word in sentences if word in model]
    ws = {w: sum([predict_proba(model, u, w) for u in sentences]) for w in sentences}
    return Counter(ws).most_common()


if __name__ == '__main__':
    corpas_path = '/Users/chenyahui/codes/python_data/word2vec/9/comment.txt'
    frequency_path = '/Users/chenyahui/codes/python_data/word2vec/9/frequency.txt'
    sentence_path = '/Users/chenyahui/codes/python_data/word2vec/9/export.txt'
    model_path = '/Users/chenyahui/codes/python_data/word2vec/9/model'
    #
    # texts = []
    # with open(corpas_path, 'r') as f:  # 采用b的方式处理可以省去很多问题
    #     reader = csv.reader(f)
    #     for row in reader:
    #         texts.append(row[1])
    #
    # with open(frequency_path, 'r') as load_f:
    #     load_dict = json.load(load_f)
    #
    # for d in load_dict:
    #     for k, v in d.items():
    #         jieba.suggest_freq(k, True)
    #
    # with open(sentence_path, 'w') as export_file:
    #     i=0
    #     i1=0
    #     for text in texts:
    #         print("cut word sentence", i, " / ", len(texts))
    #         for word in jieba.cut(text):
    #             # print("cut word word", i1)
    #             export_file.write(" " + word)
    #             i1=i1+1
    #         i=i+1
    #
    #
    # #
    # # print(load_dict)
    # # load user dict
    # # jieba.load_userdict(words_path)
    # # delete
    # # with open(corpas_path, 'r') as corpas_file:
    # #     words = jieba.cut(corpas_file.read())
    # #     with open(sentence_path, 'w') as export_file:
    # #         for word in words:
    # #             export_file.write(" " + word)
    #
    #
    # print("start")
    # sentences = word2vec.LineSentence(open(sentence_path))
    # model = Word2Vec(sentences=sentences, size=128, sorted_vocab=True)
    # model.train(sentences=sentences, total_examples=model.corpus_count, epochs=model.epochs)
    # model.save(model_path)
    # print("Yeah")

    #
    # results = model.wv.most_similar_cosmul("人民")

    # results = model.wv.similar_by_word("人民")
    # for result in results:
    #     print(result)

    # w1 = '彻底赵德汉崩溃，是被两个干警架进自己的帝京苑豪宅的。豪宅里空空荡荡，没有沙发桌椅，没有床柜厨具，厚厚的窗帘挡住外界光线，地上蒙着一层薄薄的尘埃。显然这里从未住过人。赵德汉宁愿蜗居在破旧的老房子里，也没来此享受过一天。那么这套豪宅是干吗用的？侯亮平把目光投向靠墙放着的一大排顶天立地的铁柜上。赵德汉交出一串钥匙，干警们依次打开柜门，高潮蓦然呈现在众人面前——一捆捆新旧程度不一的钞票码放整齐，重重叠叠，塞满了整排铁柜，构成了一道密不透风的钞票墙壁。这情景也许只有在大银行的金库才能见到，或者根本就是三流影视剧里的梦幻镜头。如此多的现金集中起来，对人的视觉产生了很强烈的震撼。仿佛一阵飓风袭来，让你根本无法抵御它的冲击力。所有的干警，包括侯亮平都惊呆了。  天啊，赵德汉，我想到了你贪，可想不到你这么能贪。我真服了你了，这么多钱，你一个小处长是怎么弄到手的啊？也太有手段了吧？侯亮平完全没有嘲讽的意思，蹲在赵德汉面前近乎诚恳地问。'
    # x = pd.Series(keywords(model, jieba.cut(w1)))
    # # 输出最重要的前13个词
    # print(x[0:13])

    # 分析
    model = Word2Vec.load(model_path)
    ws = model.wv.similar_by_word("格格不入", topn=100)
    for w in ws:
        print(w)

