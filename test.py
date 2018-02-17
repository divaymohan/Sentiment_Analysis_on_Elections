import re
import json
from collections import Counter
from textblob import TextBlob
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

import matplotlib.animation as animation
from matplotlib import style

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = "WA0tLIpdYD1Mqct8h6B3VNHTi"
consumer_secret = "mRXOdvqM1kmrBrIWoJhWlXAVFXjSuQLhuzy8KLAHGeGcyK1UPc"
access_token = "794403529947430912-UaR2KheAZ8OLkSfE4ZNUTp4MkRtUuQ5"
access_secret = "gEZIDYfKR9vXhvDUGvi4TjKbQcgqjZjUINFnW5vpx4Plm"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self,data):

        try:
                count = 0
                tweet= json.loads(data)
                txtblb = TextBlob(tweet["text"]).sentiment
                #print(tweet, txtblb.polarity, txtblb.subjectivity)
                if (txtblb.subjectivity * 100 > 60):
                    output = open("python1.txt", 'a')
                    output.write(str(txtblb.polarity))
                    output.write('\n')
                    output.close()
                x = txtblb.polarity

                # create a list with all the terms

                count = count + 1
                print(count)





                return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
        return True
    def on_error(self,status):
        print(status)
        return  True

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['narendra modi','modi','BJP','MODI','bhartiya janta party'])



emoticons_str = r"""
(?:
   [:=;] #Eyes
   [oO\-]? #Nose (optional)
   [D\)\]\(\]/\\OpP] #Mouth
)"""
regex_str = [
    emoticons_str,
    r'<[^>]+>',  # html tag
    r'(?:@[\w_]+)',  # @mention
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash tags
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',  # urls
    r'(?:(?:\d+,?)+(?:\,?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emotion_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emotion_re.search(token) else token.lower() for token in tokens]
    return tokens

from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english')

