# -*- coding: UTF-8 -*-

from dkword2vec.DKWord2Vec import DKWord2Vec
import json
import sys
import os


def parse_dicts(frequency_path):
    with open(frequency_path, 'r') as load_f:
        load_dict = json.load(load_f)
    print("总词量为", len(load_dict))
    result = []
    for d in load_dict:
        for key, _ in d.items():
            result.append(key)
    return result


build_model = True
if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        print("请提供目标词语")

    if len(sys.argv) > 2:
        topn = int(sys.argv[2])
    else:
        topn = 20

    data_folder = '/Users/chenyahui/codes/python_data/word2vec/9'
    corpas_path = '%s/corpas.txt' % data_folder
    word_original_path = '%s/frequency.txt' % data_folder
    token_saving_path = '%s/words.txt' % data_folder
    sentence_path = '%s/export.txt' % data_folder
    model_saving_path = '%s/model.bin' % data_folder
    msg_path='%s/juwairen_short.txt' % data_folder
    corpus_path = '%s/corpus.txt' % data_folder



    if os.path.exists(token_saving_path):
        word_list = json.load(open(token_saving_path))
    else:
        word_list = parse_dicts(word_original_path)
        with open(token_saving_path, 'w') as tf:
            tf.write(json.dumps(word_list))

    if build_model:
        word2vec = DKWord2Vec(corpus_path=corpus_path,
                              data_path=data_folder,
                              worker_size=8, word_list=word_list)
        word2vec.save(model_saving_path, bin=True)
    else:
        word2vec = DKWord2Vec.load(model_saving_path, bin=True)
        word2vec.load_predefined_words(word_list)

    tf = open(msg_path, 'r')
    text = tf.read()
    summary = word2vec.summary(text, topn=30)
    for score, text in summary:
        print(score, text)
