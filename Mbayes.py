from new import *
import nltk
import dataspliter

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(dataspliter.training_set)

Accuracy = nltk.classify.accuracy(MNB_classifier, dataspliter.testing_set)*100

def MNB_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return MNB_classifier.classify(featureset)
