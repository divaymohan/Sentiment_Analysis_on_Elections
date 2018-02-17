import re
import json
from collections import Counter
from textblob import TextBlob
import matplotlib
matplotlib.use('TkAgg')
import naiveworking
from nltk.corpus import stopwords
import string
import Mbayes
import LogisticReg
import Bbayes
import NuSVC_classifier
import hybridworking


current_window = ''
filename = ''

def setCurrentWindow(name):
    current_window = name

def getCurrentWindow():
    return current_window

def setFilename(filename):
    filename = filename
def getFilename():
    return filename


def Naive_Classify():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/Naive_Classify.txt", 'a')
                    output.write(str(naiveworking.Naive_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(naiveworking.Naive_classifier_text(tweet["text"]))
        return 'result/Naive_Classify.txt'

def MBayes():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/MNB_Classify.txt", 'a')
                    output.write(str(Mbayes.MNB_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(Mbayes.MNB_classifier_text(tweet["text"]))
    return 'result/MNB_Classify.txt'

def LogisticRegeration():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/LogisticReg.txt", 'a')
                    output.write(str(LogisticReg.LogisticRegression_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(LogisticReg.LogisticRegression_classifier_text(tweet["text"]))

    return 'result/LogisticReg.txt'

def BNB_classifier():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/BNB_classifier.txt", 'a')
                    output.write(str(Bbayes.BNB_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(Bbayes.BNB_classifier_text(tweet["text"]))
    return 'result/BNB_classifier.txt'


def NuSVC():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/NuSVC.txt", 'a')
                    output.write(str(NuSVC_classifier.NuSVC_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(NuSVC_classifier.NuSVC_classifier_text(tweet["text"]))
    return 'result/NuSVC.txt'
def Hybrid():
    punctuation = list(string.punctuation)
    stop = stopwords.words('english')
    fname = 'python.json'

    with open(fname, 'r', newline='\r\n') as f:
        count = 0
        count_all = Counter()
        for line in f:
            if line.strip():

                tweet = json.loads(line)
                txtblb = TextBlob(tweet["text"]).sentiment

                if (txtblb.subjectivity):
                    output = open("result/Hybrid.txt", 'a')
                    output.write(str(hybridworking.voted_classifier_text(tweet["text"])))

                    output.write('\n')
                    output.close()
                    print(hybridworking.voted_classifier_text(tweet["text"]))

    return 'result/Hybrid.txt'
print(NuSVC())