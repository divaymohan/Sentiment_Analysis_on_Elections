import nltk
from new import *

# documents = [(list(movie_reviews.words(fileid)), category)
#                  for category in movie_reviews.categories()
#                  for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)
# all_words = []
# for w in movie_reviews.words():
#     all_words.append(w.lower())
#
# all_words = nltk.FreqDist(all_words)
# word_features = list(all_words.keys())[:5000]
# print(all_words)
# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#
#     return features
#
# featuresets = [(find_features(rev), category) for (rev, category) in documents]
#     # set that we'll train our classifier with
# training_set = featuresets[:1900]
#
#     # set that we'll test against.
# testing_set = featuresets[1900:]
# print(training_set[1])
# short_pos = open("training_data/positive.txt","r").read()
# short_neg = open("training_data/negative.txt","r").read()
#
# # move this up here
# all_words = []
# documents = []
#
#
# #  j is adject, r is adverb, and v is verb
# allowed_word_types = ["J"]
# #allowed_word_types = ["J"]
#
# for p in short_pos.split('\n'):
#     documents.append( (p, "pos") )
#     words = word_tokenize(p)
#     pos = nltk.pos_tag(words)
#     for w in pos:
#         if w[1][0] in allowed_word_types:
#             all_words.append(w[0].lower())
# for p in short_neg.split('\n'):
#     documents.append( (p, "neg") )
#     words = word_tokenize(p)
#     pos = nltk.pos_tag(words)
#     for w in pos:
#         if w[1][0] in allowed_word_types:
#             all_words.append(w[0].lower())
# filter_word = []
# for i in all_words:
#     if len(i) > 2:
#         filter_word.append(i)
# import pickle
# save_documents = open("pickels/documents.pickle","wb")
# pickle.dump(documents, save_documents)
# save_documents.close()
# filter_word = nltk.FreqDist(filter_word)
# word_features = list(filter_word.keys())[:5000]
# save_word_features = open("pickels/word_features11k.pickle","wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()
open_pickle = open("pickels/word_features11k.pickle","rb")
word_features = pickle.load(open_pickle)
open_pickle.close()

open_pickle = open("pickels/documents.pickle","rb")
documents = pickle.load(open_pickle)
open_pickle.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)


    print(features)
    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)

training_set = featuresets[:1000]
save_pickle = open("pickels/training.pickle","wb")
pickle.dump(training_set,save_pickle)
save_pickle.close()
testing_set = featuresets[1000:2000]
save_pickle = open("pickels/testing.pickle","wb")
pickle.dump(training_set,save_pickle)
save_pickle.close()
# open_pickle = open("pickels/training.pickle","rb")
# documents = pickle.load(open_pickle)
# open_pickle.close()
#
# for item in documents:
#     print(item)