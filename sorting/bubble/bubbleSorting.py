# -*- coding:utf-8 -*-
from sorting.utils import sorting, swapElements


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
        for j in range(0, total_count - 1 - i):
            if source_list[j] > source_list[j + 1]:
                is_swapped = True
                swapElements(source_list, j, j + 1)
        if is_swapped is False:
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
        for j in range(i, total_count - 1 - i):
            if source_list[j] > source_list[j + 1]:
                is_swapped = True
                swapElements(source_list, j, j + 1)
        if is_swapped is False:
            return source_list

        is_swapped = False
        for k in range(total_count - 2 - i, i, -1):
            if source_list[k - 1] > source_list[k]:
                is_swapped = True
                swapElements(source_list, k - 1, k)
        if is_swapped is False:
            return source_list
    return source_list
