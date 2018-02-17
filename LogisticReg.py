from new import *
import dataspliter

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(dataspliter.training_set)
Accuracy = (nltk.classify.accuracy(LogisticRegression_classifier, dataspliter.testing_set))*100

def LogisticRegression_classifier_text(text):
    featureset = dataspliter.find_features(text)
    return LogisticRegression_classifier.classify(featureset)
