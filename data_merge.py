#!/usr/bin/env python
import re
import sys
file_sh = open("movie_review.txt","r")
file_sa = open("saved_tweets.txt","r")
output_file = open("output_MR.txt", "w")

for line in file_sh:
	sh_list=line.strip().split(",",1)
	for line in file_sa:
		sa_list=line.strip().split(",",1)
		if sh_list[0]==sa_list[0]:
			data=sh_list[0]+','+sh_list[1]+':'+sa_list[1]
			output_file.write(data+"\n")
output_file.close() 
	
file_sh.close()
file_sa.close()

