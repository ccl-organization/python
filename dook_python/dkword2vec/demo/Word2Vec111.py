# -*- coding: UTF-8 -*-

import os
from gensim.models import Word2Vec as WV, word2vec
import jieba
import csv
import sys


class Word2Vec(object):
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
            self._model = WV(sentences=sentences, size=vector_size, workers=worker_size, iter=10)
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

        return word2vec.LineSentence(open(sentences_path))

    @staticmethod
    def load_predefined_words(words):
        if not words:
            return

        for word in words:
            jieba.suggest_freq(word, tune=True)

    @property
    def model(self):
        return self._model

    def train(self, corpus_path):
        pass

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
    def load(model_path):
        """
        从路径里加载模型
        :param model_path: 模型的保存路径
        :return: 恢复的Word2Vec模型
        """
        wv = Word2Vec()
        wv._model = WV.load(model_path)

        return wv

    def save(self, model_path):
        """
        保存模型到目标路径
        :param model_path: 保存路径
        """
        Word2Vec.__valid_path(model_path)
        self.model.save(model_path)

    def similarity(self, word, topn=10):
        return self._model.wv.similar_by_word(word=word, topn=topn)


    if __name__ == '__main__':
        model_saving_path = '/Users/chenyahui/codes/python_data/myword2vec/model'
        # myword2vec=Word2Vec.load(model_saving_path)
        words = similarity("局外人", topn=20)

        for word in words:
            print(word)
