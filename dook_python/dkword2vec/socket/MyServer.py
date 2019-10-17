# -*- coding: utf-8 -*-

import socketserver
from dkword2vec.service.Word2vecService import Word2vecService
from dkword2vec.service import Word2vecUtil
import json

word2vecService = None
data_folder = '/Users/chenyahui/codes/python_data/word2vec/release'
# data_folder = '/Users/chenyahui/codes/python_data/word2vec/9'
corpus_path = '%s/corpus.txt' % data_folder
frequency_path = '%s/frequency.txt' % data_folder
dictionary_path = '%s/dictionary.txt' % data_folder
sentence_path = '%s/sentence.txt' % data_folder
model_saving_path = '%s/model.bin' % data_folder
msg_path = '%s/msg.txt' % data_folder


def __init():
    print('init start')
    global word2vecService
    dictionary = Word2vecUtil.parse_dicts(dictionary_path)
    word2vecService = Word2vecService.load(model_saving_path)
    word2vecService.load_predefined_words(dictionary)
    print('init over')


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes('初始化完成，请输入关键词...',encoding='utf8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            data = str(data, encoding='utf8')
            print('data  ', data)
            try:
                similarity_words = word2vecService.similarity_by_word(data)
                print("similarity_words  ", similarity_words)
                json_data = json.dumps(similarity_words, ensure_ascii=False)
                print("json_data  ", json_data)
                conn.sendall(bytes(json_data, encoding='utf8'))
            except:
                conn.sendall(bytes("不存在的词语，请重新输入", encoding='utf8'))
                print('throw exception ')
            else:
                print('success ')


if __name__ == '__main__':
    __init()
    server = socketserver .ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()


