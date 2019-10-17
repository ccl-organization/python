# -*- coding: UTF-8 -*-
print("hello")
# 示例1

from gensim.test.utils import common_texts
from gensim.models import Word2Vec

data_folder = '/Users/chenyahui/codes/python_data/myword2vec/demo'
mymode_path = '%s/mymodel' % data_folder
mymode_txt_path = '%s/mymodel.txt' % data_folder

def d1():
    print(common_texts)

    train_model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
    train_model.save(mymode_path)

    train_model.wv.save_word2vec_format(mymode_txt_path, binary=False)


#示例 2  查看词表相关信息

from gensim.test.utils import common_texts
from gensim.models import Word2Vec
def d2():
    model = Word2Vec.load(mymode_path)
    # 对于训练好的模型，我们可以通过下面这前三行代码来查看词表中的词，频度，以及索引位置，
    # 最关键的是可以通过第四行代码判断模型中是否存在这个词
    for key in model.wv.vocab:
        print(key)
        print(model.wv.vocab[key])
    print('human' in model.wv.vocab)
    print(len(model.wv.vocab)) #获取词表中的总词数


def d3():
    # 示例 5
    model = Word2Vec(sentences=pos, size=50, min_count=5)
    model.save('./vec.model_pos')
    print('语料数：', model.corpus_count)
    print('词表长度：', len(model.wv.vocab))

    # 结果

#
    # 语料数： 5000
    # 词表长度： 6699

    # -------------增量训练
    model = Word2Vec.load('./vec.model_pos ')
    model.build_vocab(sentences=neg, update=True)
    model.train(sentences=neg, total_examples=model.corpus_count, epochs=model.iter)
    model.save('./vec.model')

    print('语料数：', model.corpus_count)
    print('词表长度：', len(model.wv.vocab))
# # 结果
# 语料数： 5001
# 词表长度： 8296

# d1()
#
d2()

