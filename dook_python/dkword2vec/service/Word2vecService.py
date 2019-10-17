# -*- coding: UTF-8 -*-

import os
from gensim.models import Word2Vec, word2vec,KeyedVectors
import jieba
import csv
import re
import smart_open
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


class Word2vecService(object):
    def __init__(self, corpus_path=None, sentence_path=None,word_list=None, vector_size=128, worker_size=4):
        """
        初始化WV模型
        :param corpus_path: 语料路径
        :param word_list: 词库列表
        """
        if word_list:
            self.load_predefined_words(words=word_list)
            sentences = self.__build_sentences(corpus_path,sentence_path)
            print("开始训练模型，可能会花点时间……")
            self._model = Word2Vec(sentences=sentences, size=vector_size, workers=worker_size, iter=10)
            # self._model.train(sentences=sentences, total_examples= self._model.corpus_count, epochs= self._model.epochs)
            print("训练完成！")
        else:
            print("初始化完成！")

    @staticmethod
    def __load_predefined_words(words):
        if True:
            print("start load_predefined_words")
            if not words:
                return
            for word in words:
                jieba.suggest_freq(word, tune=True)
            print("end load_predefined_words")
        else:
            print("words is None")

    @staticmethod
    def __build_sentences(corpus_path,sentence_path):
        if not os.path.exists(sentence_path):
            print(' # 读入语料并做分词，然后保存分词文件 start ')
            sentences = []
            with open(corpus_path, 'r') as corpus_file:
                with open(sentence_path, 'w') as sentences_file:
                    reader = csv.reader(corpus_file)
                    index = 0
                    for row in reader:
                        index += 1
                        if(row is not None and len(row)):
                             print('row ',row)
                             str=jieba.cut(row[0])
                             print('str ',str)
                             sentences.append(' '.join(str))
                        if index % 10 == 0:
                            print(' sentences.clear')
                            sentences_file.write('\n'.join(sentences))
                            sentences.clear()
            print(' # 读入语料并做分词，然后保存分词文件 end ')
        else:
            print('sentences exist')
        return word2vec.LineSentence(smart_open.open(sentence_path))

    def save(self, model_path, bin=False):
        """
        保存模型到目标路径
        :param model_path: 保存路径
        :param bin: 是否用二进制的方式
        """
        Word2vecService.__valid_path(model_path)
        self._model.wv.save_word2vec_format(model_path, binary=bin)

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
        result = Word2vecService()
        result._model = KeyedVectors.load_word2vec_format(model_path, binary=bin)
        return result

    @staticmethod
    def load_predefined_words(words):
        if True :
            print("start load_predefined_words")
            if not words:
                return
            for word in words:
                jieba.suggest_freq(word, tune=True)
            print("end load_predefined_words")
        else:
            print("words is None")

    def summary(self, text, topn=3):
        if text is None:
            return None
        sentences = self.__cut_sentences(text)
        key_value = {}
        if sentences:
            for sentence in sentences:
                vector = self.__sentence_vector(sentence)
                if vector is not None:
                    key_value[sentence] = vector

        keys = list(key_value.keys())
        values = list(key_value.values())

        vector_size = len(key_value)
        similar_matrix = np.zeros([vector_size, vector_size])
        for i in range(vector_size):
            for j in range(vector_size):
                if i != j:
                    similar_matrix[i][j] = cosine_similarity(values[i].reshape(1, -1), values[j].reshape(1, -1))[0, 0]
        nx_graph = nx.from_numpy_array(similar_matrix)
        print('sentence 向量模型 创建完成')
        scores = nx.pagerank(nx_graph)
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(keys)), reverse=True)
        return ranked_sentences[0:topn]

    @staticmethod
    def __cut_sentences(text):
        cutting_tokens = '[！。？……；]'
        result = []
        for s in re.split(cutting_tokens, text):
            if len(s.strip()) > 0:
                result.append(s)
        return result

    def __sentence_vector(self, sentence):
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

    def similarity_by_word(self, word, topn=10):
        return self._model.wv.similar_by_word(word=word, topn=topn)

    def word_vector(self,word):
        try:
           return self._model.wv.get_vector(word)
        except KeyError:
            return None





