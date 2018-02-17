from matplotlib import pyplot as plt
import numpy as np
import BARgraphdata
import pandas as pd
import currentWindow

filename = currentWindow.getFilename()

data = pd.DataFrame()

positive = 0
negative = 0
neutral = 0
objects = (positive,negative,neutral)
data = pd.read_csv(filename)
data['polarity'] = data
for item in data['polarity']:
    if item == 'pos':
        positive = positive+1
    elif item == 'neg':
        negative = negative+1
    else:
        neutral = neutral+1
observation = [float(negative),float(positive),float(neutral)]


y_pos = np.arange(len(objects))
graph = plt.bar(y_pos,observation, align='center', alpha=0.5)
graph[0].set_color('r')
graph[1].set_color('g')
graph[2].set_color('b')
plt.xticks(y_pos,objects)
plt.ylabel('No of Tweet')
plt.title('Polarity of Tweets')
plt.legend((graph[0],graph[1],graph[2]), ('Negative', 'Positive','Neutral'))

fig = plt.figure(figsize=(2,2))
a = fig.add_subplot(111)
a.imshow(graph)
