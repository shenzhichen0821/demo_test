# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import copy
from sorting.utils import getRandomList
from sorting.utils import sorting


def addPlots(*_):
    pass


@sorting("insertion")
def insertionSorting(source_list):
    """
    插入排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    for i in range(1, total_count):
        index = findIndex(source_list[0: i], source_list[i])
        addPlots(source_list, index, i)
        insertIntoList(source_list, index, i, source_list[i])
        addPlots(source_list, i, i)
    return source_list


def insertIntoList(source_list, index, target, obj):
    """
    将指定元素插入target处
    :param source_list:
    :param index:
    :param target:
    :return:
    """
    source_list.insert(index, obj)
    source_list.pop(target + 1)


def findIndex(ori_list, element):
    for i in range(0, len(ori_list)):
        if element < ori_list[i]:
            return i
    return len(ori_list)


if __name__ == "__main__":
    _length = 16
    ori_list = getRandomList(_length)
    animation_list = [(copy.copy(ori_list), 0, 0)]

    def addPlots(source_list, smallest=None, current=None):
        animation_list.append((copy.copy(source_list), smallest, current))

    fig = plt.figure()
    insertionSorting(ori_list)
    rects = plt.bar(np.arange(_length), animation_list[0][0], color='c')

    def animate(i):
        index = 0
        for rect, height in zip(rects, animation_list[i][0]):
            rect.set_height(height + 1)
            pointer, end = animation_list[i][1], animation_list[i][2]
            if index < end:
                rect.set_color('orange')
            else:
                rect.set_color('c')

            if index == end:
                rect.set_color('red')
            elif index == pointer:
                rect.set_color('blue')

            index += 1
        return rects,

    anim = animation.FuncAnimation(fig, animate, frames=len(animation_list), interval=500)
    plt.show()