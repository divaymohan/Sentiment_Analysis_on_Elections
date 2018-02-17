import currentWindow as cw
from matplotlib import pyplot

def currentGraph():
    currentWindow = cw.getCurrentWindow()
    if currentWindow == 'Hybrid':
        filename = cw.Hybrid()
        return filename
    elif currentWindow == 'Binomial':
        filename = cw.BNB_classifier()
        return filename
    elif currentWindow == 'Multinomial':
        filename = cw.MBayes()
        return filename
    elif currentWindow == 'NuSVC':
        filename = cw.NuSVC()
        return filename
    elif currentWindow == 'Logistic':
        filename = cw.LogisticRegeration()
        return filename
    elif currentWindow== 'NaiveBayes':
        filename = cw.Naive_Classify()
        return filename
    else:
        print("File Name Not Found Error")


list = ['Hybrid','Binomial','Multinomial','Logistic','NaiveBayes', 'NuSVC']

for item in list:
    cw.setCurrentWindow(item)
    currentGraph()