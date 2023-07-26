import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure(figsize=(10,10))
plt.ion()
plt.show()

def regplot(slope, intercept,x,y,pauseDuration=0.2):
    plt.pause(pauseDuration)
    plt.clf()
   
    ax = fig.add_subplot(1,1,1)
    
    ax.set_axisbelow(True)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.xaxis.grid(color='gray', linestyle='dashed')
    plt.title(f"Weight = {slope:.2f}, Bias = {intercept:.2f}")
    plt.xlim(-4, 12)
    plt.ylim(-4, 12)
    plt.scatter(x,y,color="green")

    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-')
    plt.draw()

def regplotStatic(slope,intercept,x,y):
    plt.ioff()
    ax = fig.add_subplot(1,1,1)
    
    ax.set_axisbelow(True)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.xaxis.grid(color='gray', linestyle='dashed')
    plt.title(f"Weight = {slope:.2f}, Bias = {intercept:.2f}")
    plt.xlim(-4, 12)
    plt.ylim(-4, 12)
    plt.scatter(x,y,color="green")

    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-')
    plt.show()

