#!/usr/bin/env python
import re
import sys
file_shreya = open("/Users/shravspy/Documents/Sajan/movie_review.txt","r")
file_sajan = open("/Users/shravspy/Documents/Sajan/saved_tweets.txt","r")
output_file = open("/Users/shravspy/Documents/Sajan/output_MR.txt", "w")

for line in file_shreya:
	shreya_list=line.strip().split(",",1)
	for line in file_sajan:
		sajan_list=line.strip().split(",",1)
		if shreya_list[0]==sajan_list[0]:
			data=shreya_list[0]+','+shreya_list[1]+':'+sajan_list[1]
			output_file.write(data+"\n")
output_file.close() 
	
file_shreya.close()
file_sajan.close()

