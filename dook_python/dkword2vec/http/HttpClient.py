# -*- coding: UTF-8 -*-

import requests
from PIL import Image
from io import StringIO
import json


data_folder = '/Users/chenyahui/codes/python_data/word2vec/release'
# data_folder = '/Users/chenyahui/codes/python_data/word2vec/9'
corpus_path = '%s/corpus.txt' % data_folder
frequency_path = '%s/frequency.txt' % data_folder
dictionary_path = '%s/dictionary.txt' % data_folder
sentence_path = '%s/sentence.txt' % data_folder
model_saving_path = '%s/model.bin' % data_folder
msg_path = '%s/msg.txt' % data_folder


URL='http://localhosts:8888/similar'
# URL='http://192.168.3.10:8888/'

s=URL+'vector'
print(s)


similar_params = {'word': '书单狗'}
r_get_similar = requests.get('http://192.168.3.10:8888/similar',similar_params)
print('r_get_similar ...',r_get_similar.json())


#
#
# similar_params = {'word': '卡夫卡'}
# r_get_similar = requests.get(URL+'vector',similar_params)
# print('r_get_similar ...',r_get_similar.json())
#
# #
tf = open(msg_path, 'r')
msg = tf.read()
print("msg 加载完成")
summary_params={'sentences':msg,'id':'101'}
r_get_summary = requests.get(URL+'summary',summary_params)
json_data = json.dumps(summary_params, ensure_ascii=False)
print('r_get_summary ... ',r_get_summary.json())



# print('get ...',r_get.json())

# i = Image.open(StringIO(r_post_image.content))

# print('post ...',r_post.json())