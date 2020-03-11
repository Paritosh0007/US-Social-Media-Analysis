from __future__ import division, print_function
import numpy as np  
import glob
import os
import string
import nltk
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import decomposition
from gensim import corpora, models, similarities, matutils
import re
import pandas as pd
import logging
from nltk.stem.lancaster import LancasterStemmer
from wordcloud.wordcloud import WordCloud


ls = LancasterStemmer()
def gen_wordcloud(file_name):
    with open (file_name,'r') as file:
        data=file.read().lower().split("\n")
        
        words= []
        for line in data:
            for word in line.split(" "):
                words.append(word)
        """
        stemmed_words=[]
        for word in words:
            stemmed_words.append(ls.stem(word))
            #print(word)
            #print(ls.stem(word))
        print (stemmed_words)
        """
        stopwords2=['http','https',"the","say","\'trump",'co',"trump","u00eda","uf0339","udd25","u201d","u26a1","u00e9","u2019re",'realdonaldtrump','ud','nhttps','ude','potus',"udc47","n27","n19",'udd','president','amp','ryan',"'gop", "u2019s","Trump","ndr","donald","'s","'n","gop","'w","u2026","u2019t","'u2019s","u2019m","ude02","ud83c","ufe0f","ud83d","u0627","u2764","ude0d","u0644"
            ]
        stopwords = nltk.corpus.stopwords.words('english')
        words2 = []
        for w in words:
            if w not in stopwords and len(w) > 1 and w not in stopwords2:
                words2.append(w)
                
        freq = nltk.FreqDist(words2)
        freq.plot(35)
        
        text2 = ' '.join(words2)
        print (text2)
        
        wc = WordCloud(max_font_size=40).generate(text2)
        plt.figure()
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
	return words2






#NMF
def nmf(words2):
	my_vectorizer=TfidfVectorizer(stop_words='english', min_df=2)
	doc_termMatrix=my_vectorizer.fit_transform(words2)
	print (doc_termMatrix.shape)

	vocabulary=my_vectorizer.get_feature_names()
	print (len(vocabulary)) 
	print (vocabulary[-10:])
	print (vocabulary[:10])

	print ('num of documents, num of unique words')
	print (doc_termMatrix.shape)

	num_topics = 7

	clf = decomposition.NMF(n_components=num_topics, random_state=1)
	doctopic = clf.fit_transform(doc_termMatrix)
	print (num_topics, clf.reconstruction_err_)

	topic_words = []
	num_top_words =7

	print (vocabulary[100])

	for topic in clf.components_:
		#print (topic.shape, topic[:10])
		word_idx = np.argsort(topic)[::-1][:num_top_words]
		print (word_idx)
		for idx in word_idx:
			print (vocabulary[idx])
		#print


	print ('/**/' * 10 )  
		
		
	for t in range(len(topic_words)):
		print ("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
		
	print (doc_termMatrix.shape)

	for n in range(1, 6):    
		num_topics = 5*n
		num_top_words = 10
		clf = decomposition.NMF(n_components=num_topics, random_state=1)
		doctopic = clf.fit_transform(doc_termMatrix)
		print (num_topics, clf.reconstruction_err_)

	
#LDA

def lda(words2):
	logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
	logging.root.level = logging.INFO

	corpus=words2
	docs = []

	for i in corpus:
		docs.append(i.strip().split())
	dic = corpora.Dictionary(docs)
	print (dic)


	corp = [dic.doc2bow(text) for text in docs]
	print(type(corp), len(corp))

	tfidf = models.TfidfModel(corp)
	print(type(tfidf))

	corp_tfidf = tfidf[corp]
	print(type(corp_tfidf))

	NUM_TOPICS = 5
	model = models.ldamodel.LdaModel(corp_tfidf, 
									 num_topics=NUM_TOPICS, 
									 id2word=dic, 
									 update_every=1)
									 #passes=10)

	print("LDA model")
	topics_found = model.print_topics(10)
	counter = 1
	for t in topics_found:
		print("Topic #{} {}".format(counter, t))
		counter += 1

	model.print_topics()



words2=gen_wordcloud('TrumpExtractGeneral(Cleaned).txt')
nmf(words2)
lda(words2)
