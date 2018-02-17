from new import *
import LogisticReg
import Bbayes
import Mbayes
import naiveworking
import dataspliter
import NuSVC_classifier
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

voted_classifier = VoteClassifier(Mbayes.MNB_classifier,
                                  Bbayes.BNB_classifier,
                                  LogisticReg.LogisticRegression_classifier,
                                  naiveworking.classifier,
                                  NuSVC_classifier.SVC_classifier
                                  )
Accuracy = (nltk.classify.accuracy(voted_classifier, dataspliter.testing_set))*100

def voted_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return voted_classifier.classify(featureset)
