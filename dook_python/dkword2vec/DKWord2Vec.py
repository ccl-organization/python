# -*- coding: UTF-8 -*-

import os
from gensim.models import Word2Vec, word2vec, KeyedVectors
import jieba
import csv
import smart_open
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


class DKWord2Vec(object):
    def __init__(self, corpus_path=None, data_path='/tmp/wv', word_list=None, vector_size=128, worker_size=1):
        """
        初始化WV模型
        :param corpus_path: 语料路径
        :param word_list: 词库列表
        """
        if word_list:
            self.load_predefined_words(word_list)

        if corpus_path is not None:
            self.__valid_path(data_path)

            sentences = self.__build_sentences(corpus_path, data_path)
            print("开始训练模型，可能会花点时间……")
            self._model = Word2Vec(sentences=sentences, size=vector_size, workers=worker_size, iter=10)
            print("训练完成！")

    @staticmethod
    def __build_sentences(corpus_path, data_path):
        sentences_path = '%s/sentences.txt' % data_path

        if not os.path.exists(sentences_path):
            # 读入语料并做分词，然后保存分词文件
            sentences = []
            with open(corpus_path, 'r') as corpus_file:
                with open(sentences_path, 'w') as sentences_file:
                    reader = csv.reader(corpus_file)
                    index = 0
                    for row in reader:
                        index += 1
                        sentences.append(' '.join(jieba.cut(row[1])))
                        if index % 2000 == 0:
                            sentences_file.write('\n'.join(sentences))
                            sentences.clear()

        return word2vec.LineSentence(smart_open.open(sentences_path))

    @staticmethod
    def load_predefined_words(words):
        if False :
            print("start load_predefined_words")
            if not words:
                return
            for word in words:
                jieba.suggest_freq(word, tune=True)
            print("end load_predefined_words")
        else:
            print("words is None")

    @staticmethod
    def __valid_path(path):
        """
        确认路径
        :param path: 目标路径

        如果路径的父文件夹不存在，则创建它
        """
        directory_path = os.path.dirname(path)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    def load(model_path, bin=False):
        """
        从路径里加载模型
        :param model_path: 模型的保存路径
        :param bin: 是否用二进制的方式
        :return: 恢复的Word2Vec模型
        """
        result = DKWord2Vec()
        result._model = KeyedVectors.load_word2vec_format(model_path, binary=bin)
        # result = KeyedVectors.load(model_path)
        return result

    def save(self, model_path, bin=False):
        """
        保存模型到目标路径
        :param model_path: 保存路径
        :param bin: 是否用二进制的方式
        """
        DKWord2Vec.__valid_path(model_path)
        self._model.wv.save_word2vec_format(model_path, binary=bin)

    def similarity_by_word(self, word, topn=10):
        return self._model.wv.similar_by_word(word=word, topn=topn)

    @staticmethod
    def cut_sentences(text):
        cutting_tokens = '[！。？……；]'
        result = []
        for s in re.split(cutting_tokens, text):
            if len(s.strip()) > 0:
                result.append(s)
        return result

    def sentence_vector(self, sentence):
        if sentence is None:
            return None
        vector = []
        index = 0
        for word in jieba.cut(sentence):
            index += 1
            try:
                vector.append(self._model.wv.get_vector(word))
            except KeyError:
                # print("空词", word)
                continue

        if len(vector) > 0:
            # 把向量转成数组
            v = np.array(vector)
            # 求数组的平均值
            return np.mean(v, axis=0)
        else:
            return None

    def summary(self, text, topn=3):
        if text is None:
            return None

        sentences = self.cut_sentences(text)
        key_value = {}
        if sentences:
            for sentence in sentences:
                vector = self.sentence_vector(sentence)
                if vector is not None:
                    key_value[sentence] = vector

        keys = list(key_value.keys())
        values = list(key_value.values())

        vector_size = len(key_value)
        similar_matrix = np.zeros([vector_size, vector_size])
        for i in range(vector_size):
            for j in range(vector_size):
                if i != j:

                    s2=values[i]
                    s1=values[i].reshape(1, -1)
                    # print(s2)
                    # print(s1)
                    similar_matrix[i][j] = cosine_similarity(values[i].reshape(1, -1), values[j].reshape(1, -1))[0, 0]

        # print(similar_matrix)
        nx_graph = nx.from_numpy_array(similar_matrix)
        scores = nx.pagerank(nx_graph)

        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(keys)), reverse=True)
        return ranked_sentences[0:topn]


