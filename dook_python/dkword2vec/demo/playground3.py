# -*- coding: UTF-8 -*-

import jieba
from gensim.models import Word2Vec, word2vec
import csv
import json

# ############################above is the common pare for playground#############

def sort_by_value(input_dict, desc=True):
    items = input_dict.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort(reverse=desc)
    return [backitems[i][1] for i in range(0, len(backitems))], [backitems[i][0] for i in range(0, len(backitems))]


generating_data = False
training = False
applying = True

if __name__ == '__main__':
    data_folder = '/Users/chenyahui/codes/python_data/myword2vec/9'
    corpas_path = '%s/corpas.txt' % data_folder
    frequency_path = '%s/frequency.txt' % data_folder
    words_path = '%s/words.txt' % data_folder
    sentence_path = '%s/export.txt' % data_folder
    model_path = '%s/model' % data_folder

    if generating_data:
        # 载入词频
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

    if training:
        print('正在读入语料……')
        sentences = word2vec.LineSentence(open(sentence_path))
        print('正在生成实例……')
        model = Word2Vec(sentences=sentences, size=128, sorted_vocab=True, workers=8)
        print("Total Examples", model.corpus_count, "Epoch", model.epochs)
        model.train(sentences=sentences, total_examples=model.corpus_count, epochs=model.epochs)
        model.save(model_path)
        print("训练完成！")

    if applying:
        model = Word2Vec.load(model_path)
        results = model.wv.similar_by_word("人民")
        print(111)
        for result in results:
            print(result)

        print(222)
        # results = model.similar_by_word("人民")
        results = model.wv.doesnt_match("沙瑞金 高育良 李达康 刘庆祝".split())
        for result in results:
            print(result)



    print("完成了！")

