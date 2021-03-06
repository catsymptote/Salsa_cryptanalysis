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


def multi_line_chart(
        lines:list,
        increment=1,
        title='',
        x_label='rounds',
        y_label='Hamming distance',
        vertical_lines:list=None,
        dotted=True,
        line_labels:list = None
    ):
    assert type(lines) is list
    if type(lines[0]) is not list:
        lines = [lines]

    if len(lines) > 1:
        for i in range(len(lines) - 1):
            assert len(lines[i]) == len(lines[i+1])

    # Create x-labels.
    xs = range(0, len(lines[0])*increment, increment)

    
    if not dotted:
        for i in range(len(lines)):
            plt.plot(xs, lines[i], label=str(i))#, marker='.')
    else:
        linestyles = ['-', '--', '-.', ':']
        for i in range(len(lines)):
            linestyle_index = i % len(linestyles)
            plt.plot(xs, lines[i], label=str(i), color='black', linestyle=linestyles[linestyle_index])
            

    if vertical_lines is not None:
        for line in vertical_lines:
            if not dotted:
                plt.axvline(x=line, color='red', linestyle='--')
            else:
                plt.axvline(x=line, color='black', linestyle='--')


    #if line_labels is not None and len(line_labels) == len(lines):
    #    print('Yay!')
    #    plt.legend(lines, line_labels)
    #else:
    #    print('Nay!')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.title(title)
    plt.show()
