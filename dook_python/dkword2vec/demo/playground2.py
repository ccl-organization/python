# -*- coding: UTF-8 -*-

import tensorflow as tf
# from pypinyin import pinyin, Style
import numpy as np


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
    corpas_path = '/Users/chenyahui/codes/python_data/word2vec/9/corpus.txt'
    frequency_path = '/Users/chenyahui/codes/python_data/word2vec/9/frequency.txt'
    words_path = '/Users/chenyahui/codes/python_data/word2vec/9/words.txt'
    sentence_path = '/Users/chenyahui/codes/python_data/word2vec/9/export.txt'
    model_path = '/Users/chenyahui/codes/python_data/word2vec/9/model'

    # # 载入词频
    print("正在加载词频库……")
    with open(frequency_path, 'r') as load_f:
        load_dict = json.load(load_f)

    print("总词量为", len(load_dict))
    # 载入到结巴程序里

    print("正在给结巴设置预设词……")
    for d in load_dict:
        for k, v in d.items():
            jieba.suggest_freq(k, True)

    # 释放内存
    del load_dict

    # 读入语料
    print("正在拆词……")
    with open(corpas_path, 'r') as f:
        reader = csv.reader(f)
        # 打开分词结果导出文件
        with open(sentence_path, 'w') as export_file:
            for row in reader:
                for word in jieba.cut(row[1]):
                    export_file.write(" " + word)

        print("输出分词完成")

    print('正在读入语料……')
    sentences = word2vec.LineSentence(open(sentence_path))
    print('正在生成实例……')
    model = Word2Vec(sentences=sentences, size=128, sorted_vocab=True)
    print("Total Examples", model.corpus_count, "Epoch", model.epochs)
    model.train(sentences=sentences, total_examples=model.corpus_count, epochs=model.epochs)
    model.save(model_path)
    print("训练完成！")

    #
    results = model.wv.most_similar_cosmul("人民")

    print(model.wv.similarity('周瑜', '孙策'))

    # results = model.wv.similar_by_word("人民")
    # for result in results:
    #     print(result)

    # w1 = '彻底赵德汉崩溃，是被两个干警架进自己的帝京苑豪宅的。豪宅里空空荡荡，没有沙发桌椅，没有床柜厨具，厚厚的窗帘挡住外界光线，地上蒙着一层薄薄的尘埃。显然这里从未住过人。赵德汉宁愿蜗居在破旧的老房子里，也没来此享受过一天。那么这套豪宅是干吗用的？侯亮平把目光投向靠墙放着的一大排顶天立地的铁柜上。赵德汉交出一串钥匙，干警们依次打开柜门，高潮蓦然呈现在众人面前——一捆捆新旧程度不一的钞票码放整齐，重重叠叠，塞满了整排铁柜，构成了一道密不透风的钞票墙壁。这情景也许只有在大银行的金库才能见到，或者根本就是三流影视剧里的梦幻镜头。如此多的现金集中起来，对人的视觉产生了很强烈的震撼。仿佛一阵飓风袭来，让你根本无法抵御它的冲击力。所有的干警，包括侯亮平都惊呆了。  天啊，赵德汉，我想到了你贪，可想不到你这么能贪。我真服了你了，这么多钱，你一个小处长是怎么弄到手的啊？也太有手段了吧？侯亮平完全没有嘲讽的意思，蹲在赵德汉面前近乎诚恳地问。'
    # x = pd.Series(keywords(model, jieba.cut(w1)))
    # # 输出最重要的前13个词
    # print(x[0:13])

    # model = Word2Vec.load(model_path)
    # ws = model.similarity("刘慈欣", "大刘")
    # print(ws)
    # ws = model.wv.similar_by_word("文青", topn=20)
    # for w in ws:
    #     print(w)

