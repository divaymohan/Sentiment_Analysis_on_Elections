import nltk
from new import *


open_pickle = open("pickels/word_features11k.pickle","rb")
word_features = pickle.load(open_pickle)
open_pickle.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    print(features)
    return features


# training_set = featuresets[:1000]
# save_pickle = open("pickels/training.pickle","wb")
# pickle.dump(training_set,save_pickle)
# save_pickle.close()
# testing_set = featuresets[1000:2000]
# save_pickle = open("pickels/testing.pickle","wb")
# pickle.dump(training_set,save_pickle)
# save_pickle.close()
open_pickle = open("pickels/training.pickle","rb")
training_set = pickle.load(open_pickle)
open_pickle.close()



open_pickle = open("pickels/testing.pickle","rb")
testing_set = pickle.load(open_pickle)
open_pickle.close()


