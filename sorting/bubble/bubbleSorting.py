# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import copy
from sorting.utils import getRandomList
from sorting.utils import sorting, swapElements


def addPlots(*_):
    pass

@sorting("bubble")
def bubbleSorting(source_list):
    """
    简单冒泡排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    if total_count < 2:
        return source_list
    for i in range(0, total_count):
        is_swapped = False
        addPlots(source_list, 0)
        for j in range(0, total_count - 1 - i):
            if source_list[j] > source_list[j + 1]:
                is_swapped = True
                swapElements(source_list, j, j + 1)
            addPlots(source_list, j + 1)
        if not is_swapped:
            return source_list
    return source_list


@sorting("bubbleUpgrade")
def bubbleUpgradeSorting(source_list):
    """
    鸡尾酒排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    if total_count < 2:
        return source_list
    for i in range(0, int(total_count / 2 + total_count % 2)):
        is_swapped = False
        addPlotsEx(source_list, i)
        for j in range(i, total_count - 1 - i):
            if source_list[j] > source_list[j + 1]:
                is_swapped = True
                swapElements(source_list, j, j + 1)
            addPlotsEx(source_list, j + 1)
        if not is_swapped:
            return source_list

        is_swapped = False
        addPlotsEx(source_list, total_count - 2 - i)
        for k in range(total_count - 2 - i, i, -1):
            if source_list[k - 1] > source_list[k]:
                is_swapped = True
                swapElements(source_list, k - 1, k)
            addPlotsEx(source_list, k - 1)
        if not is_swapped:
            return source_list
    return source_list


if __name__ == "__main__":
    _length = 16

    # bubbleSorting
    ori_list = getRandomList(_length)
    animation_list = [(copy.copy(ori_list), 0)]

    def addPlots(source_list, index):
        animation_list.append((copy.copy(source_list), index))

    fig_0 = plt.figure()
    bubbleSorting(ori_list)
    rects = plt.bar(np.arange(_length), animation_list[0][0], color='c')

    def animate(i):
        index = 0
        for rect, height in zip(rects, animation_list[i][0]):
            rect.set_height(height + 1)
            if index == animation_list[i][1]:
                rect.set_color('blue')
            else:
                rect.set_color('c')
            index += 1
        return rects,


    # bubbleUpgradeSorting
    ori_list_1 = getRandomList(_length)
    animation_list_1 = [(copy.copy(ori_list_1), 0)]

    def addPlotsEx(source_list, index):
        animation_list_1.append((copy.copy(source_list), index))

    fig_1 = plt.figure()
    bubbleUpgradeSorting(ori_list_1)
    rects_1 = plt.bar(np.arange(_length), animation_list_1[0][0], color='c')

    def animateEx(i):
        index = 0
        for rect, height in zip(rects_1, animation_list_1[i][0]):
            rect.set_height(height + 1)
            if index == animation_list_1[i][1]:
                rect.set_color('blue')
            else:
                rect.set_color('c')
            index += 1
        return rects,


    anim_0 = animation.FuncAnimation(fig_0, animate, frames=len(animation_list), interval=250)
    anim_1 = animation.FuncAnimation(fig_1, animateEx, frames=len(animation_list_1), interval=250)
    plt.show()
