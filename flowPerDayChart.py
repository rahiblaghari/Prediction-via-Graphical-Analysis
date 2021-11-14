# import matplotlib and use to create live graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#configure graph to make it suitable for live updating
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i): #reprint graph with new points, otherwise would have overlapping lines and random colors
    graph_data = open('plotted.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    plt.title("Flow Rate vs Time Chart")
    plt.xlabel("Time (days)")
    plt.ylabel("Flow Rate (bbl/day)")
    plt.plot(xs, ys)
# animate then print out graph, as points added to file the graph will update
ani = animation.FuncAnimation(fig, animate)
plt.show()