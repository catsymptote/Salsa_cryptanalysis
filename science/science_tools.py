import matplotlib.pyplot as plt
import math


def bar_chart(values:list, titles=None, title='', x_label='x', y_label='y'):
    if titles is None:
        titles = []
        for i in range(len(values)):
            if i%(int(len(values)/10))==0:
                titles.append(str(i))
            else:
                titles.append(' ')#str(i))

    x_pos = [i for i, _ in enumerate(values)]
    
    plt.style.use('ggplot')
    plt.bar(x_pos, values, color='green')#, width=1.0)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(x_pos, titles)
    plt.show()
