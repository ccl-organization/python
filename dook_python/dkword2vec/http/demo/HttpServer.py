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
        elif "wordVector" == method:
            print('wordVector start...')
            sentences = parse_qs(params)['word'][0]
            try:
                wordVector = word2vecService.summary(sentences, 50)
                print("summary  ", summary)
                json_data = json.dumps(summary, ensure_ascii=False)
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


    def do_POST(self):
        print('do post start ')
        enc = "UTF-8"
        # mpath,margs=urllib.request.splitquery(self.path)
        # datas = self.rfile.read(int(self.headers['content-length']))
        # print('111',  mpath,margs,datas)
        path = str(self.path)  # 获取请求的url
        # length = int(self.headers.getheader('content-length'))  # 获取除头部后的请求参数的长度
        length=int(self.headers['content-length'])
        # 获取请求参数数据，请求数据为json字符串
        # datas = parse_qs(self.rfile.read(length), keep_blank_values=1)
        datas = self.rfile.read(length)
        # params=datas[2:]
        print('datas   ', datas)
        # print(params)
        # print(datas.encode(encoding="utf-8").decode(encoding="utf-8"))  # unicode编码转换为utf-8编码，再转化为unicode编码
        datas2 = unquote(datas).decode("utf-8", 'ignore')
        datas2 = unquote(datas, encoding='gbk', errors='replace')
        print('datas   ',datas2)
        if path == "/summary":
            sentences = datas["sentences"][0]  # 获取models参数数据
            print('sentences  ',sentences )
            print('可以添加对参数的逻辑处理')
            # 以下是返回报文
            self.send_response(200)  # 返回状态码
            self.send_header("Content-type", "text/html;charset=%s" % enc)  # 返回响应头内容
            self.end_headers()  # 返回响应头结束
            buf = {"status": 0,  # 返回包体数据
                   "data": {
                       "filepath": "上传答题卡成功"}}
            self.wfile.write(json.dumps(buf))  # 发送json格式的返回包体


if __name__ == '__main__':
    __init()
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
