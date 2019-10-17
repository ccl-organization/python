# -*- coding: UTF-8 -*-
import numpy

categories = ['alt.atheism', 'soc.religion.christian',
             'comp.graphics', 'sci.med']

from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train',
     categories=categories, shuffle=True, random_state=42)
print 'start'
print("\n".join(twenty_train.data[0].split("\n")[:3]))

ary1=twenty_train.target[:10]

for t in twenty_train.target[:10]:
    print(twenty_train.target_names[t])
    
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts2 = count_vect.fit_transform(twenty_train.data[:3])
X_train_counts3 = count_vect.fit_transform(twenty_train.data[:1])
s1=X_train_counts.shape

list1 = numpy.array(['physics aaa 好的', 'physics aaa 好的'])
X_train_counts4 = count_vect.fit_transform(list1)

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
tfidf_transformer = TfidfTransformer()
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))
# ...
# 'God is love' => soc.religion.christian
# 'OpenGL on the GPU is fast' => comp.graphics

print X_train_counts2
print 'xxx'
print X_train_counts3
print

