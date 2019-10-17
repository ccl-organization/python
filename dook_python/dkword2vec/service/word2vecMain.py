# -*- coding: UTF-8 -*-

from dkword2vec.service.Word2vecService import Word2vecService
from dkword2vec.service import Word2vecUtil

#
# data_folder = '/Users/chenyahui/codes/python_data/word2vec/release'

data_folder = '/Users/chenyahui/codes/python_data/word2vec/sanguo'
# data_folder = '/Users/chenyahui/codes/python_data/word2vec/9'
corpus_path = '%s/corpus.txt' % data_folder
frequency_path = '%s/frequency.txt' % data_folder
dictionary_path = '%s/dictionary.txt' % data_folder
sentence_path = '%s/sentence.txt' % data_folder
model_saving_path = '%s/model.bin' % data_folder
msg_path = '%s/msg.txt' % data_folder

build_model=False


if __name__ == '__main__':
    print("start... ")
    dictionary=Word2vecUtil.parse_dicts(dictionary_path)
    if build_model:
        word2vecService=Word2vecService(corpus_path=corpus_path,sentence_path=sentence_path,word_list=dictionary, vector_size=128, worker_size=8)
        word2vecService.save(model_saving_path)
    else:
        word2vecService=Word2vecService.load(model_saving_path)
        word2vecService.load_predefined_words(dictionary)
    print('获取核心句子')
    tf = open(msg_path, 'r')
    msg = tf.read()
    print("msg 加载完成")
    summary=word2vecService.summary(msg,30)
    for score, text in summary:
        print(score, text)

    print('获取相似词')
    similarity_words=word2vecService.similarity_by_word("吕布")
    s1=  word2vecService._model.wv.similarity('吕布','貂蝉')
    for score,text in similarity_words:
        print(score,text)

    print('寻找对应关系')

    y4 = word2vecService._model.most_similar(['吕布', '貂蝉'], ['周瑜'], topn=3)
    for item in y4:
        print(item[0], item[1])

    print("over...")


