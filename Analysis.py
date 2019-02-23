#!/usr/bin/env python 

import nltk
import sys
#import time
import textblob
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from textblob import TextBlob 

def removing_stop_words():
	file = open("/Users/shravspy/Documents/RBDA/Assignments/Project/Analytics/Analytics_code/output_MR.txt", "r")
	output_file = open("/Users/shravspy/Documents/RBDA/Assignments/Project/Analytics/Analytics_code/output_sw.txt", "w")
	stop_words = set(stopwords.words('english'))
	word_tokens=[]

	for line in file:
		line = line.split(",")
		sentence=line[1].split(":")
		list_each_sentence=[]
		for i in range(0,len(sentence)):
			line_each = sentence[i].lower()
			word_tokens = word_tokenize(line_each)
			filtered_sentence = [w for w in word_tokens if not w in stop_words] 
			wo_sentence=''
			for i in range (0,len(filtered_sentence)):
				if i==0:
					wo_sentence=wo_sentence + str(filtered_sentence[i])
				else:
					wo_sentence=wo_sentence + ' ' +str(filtered_sentence[i])
			list_each_sentence.append(wo_sentence)
		final = ":".join(list_each_sentence)
 
		output_file.write(line[0]+ ","+final + "\n") #this will put the info in the file

	output_file.close() 
	
	file.close()
	#time.sleep(10)

def sentiment_analysis():
	counter_positive=0
	counter_neutral=0
	counter_negative=0
	file = open("/Users/shravspy/Documents/RBDA/Assignments/Project/Analytics/Analytics_code/output_sw.txt", "r")
	output_file = open("/Users/shravspy/Documents/RBDA/Assignments/Project/Analytics/Analytics_code/output_pnn.txt", "w")
	for line in file:
		line=line.split(',')
		sentence=line[1].split(":")
		for i in range(0,len(sentence)):
			analysis = TextBlob(sentence[i]) 
		# set sentiment 
			if analysis.sentiment.polarity > 0: 
				#print(sentence[i],' positive')
				counter_positive=counter_positive+1
			elif analysis.sentiment.polarity == 0: 
				#print(sentence[i],' neutral')
				counter_neutral=counter_neutral+1
			else: 
				#print(sentence[i],' negative')
				counter_negative=counter_negative+1
		#print(line[0]+":"+"Number of positive, negative, neutral sentences are"+":" + str(counter_positive)+":"+str(counter_negative)+":"+str(counter_neutral))
		Total_reviews= counter_neutral+counter_negative+counter_positive
		output_file.write(line[0]+":"+"Number of positive, negative, neutral and total sentences are"+":" + str(counter_positive)+":"+str(counter_negative)+":"+str(counter_neutral)+":"+str(Total_reviews)+"\n") #this will put the info in the file

	output_file.close() 
	
	file.close()
		#print(line[0]+":""Number of negative sentences are" + ":" +str(counter_negative))
		#print(line[0]+":""Number of neutral sentences are" +":" + str(counter_neutral))

removing_stop_words()
sentiment_analysis()