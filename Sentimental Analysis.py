# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:01:49 2017

@author: parithy
"""


import tweepy
from tweepy import Stream
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey=# enter the key details
csecret= ####3
atoken=##########
asecret=#########

class listener(StreamListener):

    def on_data(self, data):
        try:
            tweet =data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            saveFile = open('tweet.txt' , 'a')
            saveFile.write(tweet)
            saveFile.write('\n')
            saveFile.close()
            #print(data)
            
            return(True)
        except BaseException:
            print('Failed')

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["india"])
