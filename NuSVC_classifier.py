from new import *
import nltk
import dataspliter

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(dataspliter.training_set)
Accuracy = (nltk.classify.accuracy(SVC_classifier, dataspliter.testing_set))*100

def NuSVC_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return SVC_classifier.classify(featureset)

