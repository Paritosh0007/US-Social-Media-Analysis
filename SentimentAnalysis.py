from __future__ import division
from textblob import TextBlob
import string
import nltk
#import preprocessor as p1
import matplotlib.pyplot as plt
def sent_analysis(file_name):
	with open(file_name,'r') as f:
		lines=f.readlines()
	 
	# start of sentiment analysis
	sub_list=[]
	pol_list=[]
	for line in lines:
		s_pos = line
		tb_pos = TextBlob(s_pos)
		sub_list.append(tb_pos.sentiment.subjectivity)
		pol_list.append(tb_pos.sentiment.polarity)
		sub_avg= sum(sub_list) / float(len(sub_list))
		pol_avg= sum(pol_list) / float(len(pol_list))
		
	print (len(sub_list))
	#print(pol_list)
		
	plt.hist(sub_list, bins=20) 
	plt.xlabel('subjectivity score')
	plt.ylabel('tweet count')
	plt.grid(True)
	#plt.savefig('subjectivity.pdf')
	plt.show()   

	plt.hist(pol_list, bins=20) 
	plt.xlabel('polarity score')
	plt.ylabel('tweet count')
	plt.grid(True)
	#plt.savefig('polarity.pdf')
	plt.show() 

	print ('the average of subjectivity scores is {}'.format(sub_avg))
	print ('the average of polarity scores is {}'.format(pol_avg))
	
# End of sentiment analysis
	
sent_analysis('TrumpExtractGeneral(Cleaned)')
