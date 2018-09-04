# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import copy
from sorting.utils import sorting
from sorting.utils import getRandomList


def addPlots(*_):
    pass


@sorting("quick")
def quickSorting(source_list):
    """
    快速排序
    :param source_list:
    :return:
    """
    recursiveDivide(source_list, 0, len(source_list) - 1)
    return source_list


def recursiveDivide(ori_list, start_index, end_index):
    if start_index >= end_index:
        return

    tail_index = start_index
    for index in range(start_index, end_index):
        addPlots(ori_list, tail=tail_index, index=index, end=end_index)
        if ori_list[index] <= ori_list[end_index]:
            ori_list.insert(tail_index, ori_list.pop(index))
            tail_index += 1

    addPlots(ori_list, end=end_index)
    ori_list.insert(tail_index, ori_list.pop(end_index))
    addPlots(ori_list, end=tail_index)

    recursiveDivide(ori_list, start_index, tail_index - 1)
    recursiveDivide(ori_list, tail_index + 1, end_index)


if __name__ == "__main__":
    _length = 16
    ori_list = getRandomList(_length)
    animation_list = []

    def addPlots(source_list, tail=None, index=None, end=None):
        animation_list.append((copy.copy(source_list), tail, index, end))

    addPlots(copy.copy(ori_list))
    fig = plt.figure()
    quickSorting(ori_list)
    rects = plt.bar(np.arange(_length), animation_list[0][0], color='c')

    def animate(i):
        index = 0
        for rect, height in zip(rects, animation_list[i][0]):
            tail, current, end = animation_list[i][1], animation_list[i][2], animation_list[i][3]
            rect.set_height(height + 1)

            if (end is not None and tail is not None) and (end > index > tail):
                rect.set_color('yellow')
            else:
                rect.set_color('c')

            if index == current and index != tail:
                rect.set_color('blue')
            elif index == tail:
                rect.set_color('orange')
            elif index == end:
                rect.set_color('red')

            index += 1
        return rects,

    anim = animation.FuncAnimation(fig, animate, frames=len(animation_list), interval=500)
    plt.show()