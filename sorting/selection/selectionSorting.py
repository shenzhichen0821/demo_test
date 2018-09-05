# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import copy
from sorting.utils import getRandomList
from sorting.utils import sorting, swapElements


def addPlots(*_):
    pass


@sorting("selection")
def selectionSorting(source_list):
    """
    简单选择排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    for i in range(0, total_count):
        smallest_index = i
        addPlots(source_list, None, smallest_index)
        for j in range(i + 1, total_count):
            if source_list[j] < source_list[smallest_index]:
                smallest_index = j
            addPlots(source_list, smallest_index, j)
        addPlots(source_list, smallest_index, i)
        if smallest_index != i:
            swapElements(source_list, i, smallest_index)
        addPlots(source_list, i, smallest_index)
    return source_list


if __name__ == "__main__":
    _length = 16
    ori_list = getRandomList(_length)
    animation_list = [(copy.copy(ori_list), 0, 0)]

    def addPlots(source_list, smallest=None, current=None):
        animation_list.append((copy.copy(source_list), smallest, current))

    fig = plt.figure()
    selectionSorting(ori_list)
    rects = plt.bar(np.arange(_length), animation_list[0][0], color='c')

    def animate(i):
        index = 0
        for rect, height in zip(rects, animation_list[i][0]):
            rect.set_height(height + 1)
            smallest, current = animation_list[i][1], animation_list[i][2]
            if index == smallest:
                rect.set_color('red')
            elif index == current:
                rect.set_color('blue')
            else:
                rect.set_color('c')
            index += 1
        return rects,

    anim = animation.FuncAnimation(fig, animate, frames=len(animation_list), interval=500)
    plt.show()