# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:07:47 2017

@author: parithy
"""

from textblob import TextBlob
import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser
import json



#consumer key, consumer secret, access token, access secret.
ckey=#provide the key details
csecret=
atoken=
asecret=

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#api=tweepy.API(auth)
api= tweepy.API(auth, parser=JSONParser())

#trend1 =api.trends_place(1)
#print(trend1)


public_tweets = api.search(q='trump' ,count=1 ,since_date = "2017-02-19")
print(public_tweets)
#print (public_tweets)

#for i in public_tweets :
##!    print(i.text , i.user)
#    print(i)
##    j=json.loads(_json)
#    print(j)    
#    analysis = TextBlob(i.text)
#    print(analysis.sentiment.polarity)


#test = TextBlob("parithy is a very nice guy , very good guy , very patient")

#print (test.tags)
#print (test.words)
#print (test.sentiment.polarity)
