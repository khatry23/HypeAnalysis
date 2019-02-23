#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from twython import TwythonStreamer  
import csv
import json

credentials = {}  
credentials['CONSUMER_KEY'] = "YfzVcvnKzOrCb1Rewrhs51I8K"
credentials['CONSUMER_SECRET'] = "mWD3p3SRaGjgDQG7LGWUPIIwo5XZmOHTB5jgUUE18tg3dz9aVU"  
credentials['ACCESS_TOKEN'] = "1047290910353051653-sa1ouTDporzgNkExyT0I4wSRgrvm0J"  
credentials['ACCESS_SECRET'] = "RTbK7PoD0CiCtdoByptlk3pi16EejgFH8P9y8oMaeNAoT"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)


# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)
# Filter out unwanted data
def process_tweet(tweet):  
    d = {}
    #d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    #d['user'] = tweet['user']['screen_name']
    #d['user_loc'] = tweet['user']['location']
    d['date']=tweet['user']['created_at']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
            
            # Instantiate from our streaming class
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],  
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
# Start the stream
stream.statuses.filter(track='ThugOfHindostan')  
