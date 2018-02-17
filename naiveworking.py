from new import *
import nltk
import dataspliter

classifier = nltk.NaiveBayesClassifier.train(dataspliter.training_set)
Accuracy = (nltk.classify.accuracy(classifier, dataspliter.testing_set))*100

def Naive_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return classifier.classify(featureset)
