# -*- coding: UTF-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from dkword2vec.service.Word2vecService import Word2vecService
from dkword2vec.service import Word2vecUtil
import urllib.request
from urllib.parse import urlparse, parse_qs, unquote
import urllib.parse

word2vecService = None
data_folder = '/Users/chenyahui/codes/python_data/word2vec/release'
# data_folder = '/Users/chenyahui/codes/python_data/word2vec/9'
corpus_path = '%s/corpus.txt' % data_folder
frequency_path = '%s/frequency.txt' % data_folder
dictionary_path = '%s/dictionary.txt' % data_folder
sentence_path = '%s/sentence.txt' % data_folder
model_saving_path = '%s/model.bin' % data_folder
msg_path = '%s/msg.txt' % data_folder

data = {'result': 'this is a test'}
host = ('localhost', 8888)


def __init():
    print('init start')
    global word2vecService
    dictionary = Word2vecUtil.parse_dicts(dictionary_path)
    word2vecService = Word2vecService.load(model_saving_path)
    word2vecService.load_predefined_words(dictionary)
    print('init over')


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        data = None
        query = urllib.request.splitquery(self.path)
        method = query[0].replace(' ', '').replace("/", '')
        params = query[1]
        print('method ', method)
        # 获取相似词
        if "similar" == method:
            print('similar start...')
            word = parse_qs(params)['word'][0]
            try:
                similarity_words = word2vecService.similarity_by_word(word)
                print("similarity_words  ", similarity_words)
                json_data = json.dumps(similarity_words, ensure_ascii=False)
                print("json_data  ", json_data)
                data = json_data
            except:
                data = "不存在的词语，请重新输入"
                print('throw exception ')
        # 获取概要
        elif "summary" == method:
            print('summary start...')
            sentences = parse_qs(params)['sentences'][0]
            try:
                summary = word2vecService.summary(sentences, 50)
                print("summary  ", summary)
                json_data = json.dumps(summary, ensure_ascii=False)
                print("json_data  ", json_data)
                data = json_data
            except:
                data = "不存在的词语，请重新输入"
                print('throw exception ')
        # 获取词向量
        elif "vector" == method:
            print('vector start...')
            word = parse_qs(params)['word'][0]
            try:
                vector = word2vecService.word_vector(word)
                print("vector  ", vector)
                json_data = json.dumps(vector.tolist(), ensure_ascii=False)
                # json_data=vector
                print("json_data  ", json_data)
                data = json_data
            except:
                data = "不存在的词语，请重新输入"
                print('throw exception ')
        else:
            data = 'no such method '
            print('no such method...')
        print(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


if __name__ == '__main__':
    __init()
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
