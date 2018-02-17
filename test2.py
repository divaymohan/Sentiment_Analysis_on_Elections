import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from pylab import *
import numpy as np
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)



def animate(i):
    graph_data = open('python1.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    # ys = []


    for line in lines:
        x = line
        xs.append(x)
    # X, Y = meshgrid(xs, ys)
    # z1 = bivariate_normal(X,Y,1.0,1.0,0.0,0.0)
    # z2 = bivariate_normal(X,Y,1.5,0.5,1,1)
    # Z = 10*(z1-z2)

    # original = 'lower'
    # CS = contourf(x,y,Z,10,#[-1,-0.1,0,0.1],
    #               cmap=cm.bone,
    #               origin = original)
    title('nonsense')
    xlabel('x axis')
    ylabel('y axis')
    ax1.clear()
    ax1.plot(xs)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.ylim(-1,1)
plt.xlim(1,500)

