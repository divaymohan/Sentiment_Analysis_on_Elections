from new import *
import nltk
import dataspliter

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(dataspliter.training_set)
Accuracy = nltk.classify.accuracy(BNB_classifier, dataspliter.testing_set)*100

def BNB_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return BNB_classifier.classify(featureset)

