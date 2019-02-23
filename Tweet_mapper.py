#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python
import re
import sys
file = open("/Users/shravspy/Documents/Sajan/saved_tweets.csv","r")

def clean_tweet(tweet):
    if 'http' in tweet:
        tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    if "RT" or "cc" in tweet:
        tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    if "#" in tweet:
        tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    if "@" in tweet:
        tweet = re.sub('@\S+', '', tweet)  # remove mentions
    
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet


#for line in sys.stdin:
for line in file:
    if ',' in line:
        line = line.rsplit(",",1)
        full_date=line[1].split(" ")
        #print full_date
        list_month=['Jan','Feb','Mar','Apr', 'May','Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for i in range(0,len(list_month)):
            if list_month[i]==full_date[1]:
                month=i+1
                date= full_date[5].strip()+'-'+str(month)+'-'+full_date[2]
                (date_key, val)=(date,clean_tweet(line[0]))
                print"%s,%s"%(date_key,val)
            else:
                continue
   
    
    
    
    
    
    
    
    
