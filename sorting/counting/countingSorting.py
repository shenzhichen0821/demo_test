# -*- coding:utf-8 -*-
from sorting.utils import sorting


@sorting("counting unstable")
def countingUnstableSorting(source_list):
    """
    计数排序，仅适用正整数序列，不稳定排序
    :param source_list:
    :return:
    """
    index_list = [0 for _ in range(0, len(source_list))]
    for index in range(0, len(source_list)):
        index_list[index] += 1
    source_list = []
    for index in range(0, len(index_list)):
        source_list.extend([index for _ in range(0, index_list[index])])
    return source_list


@sorting("counting stable")
def countingStableSorting(source_list):
    """
    计数排序，仅适用正整数序列，稳定排序
    :param source_list:
    :return:
    """
    index_list = []
    for index in range(0, len(source_list)):
        element = source_list[index]
        if len(index_list) < (element + 1):
            index_list.extend([0 for _ in range(element - len(index_list) + 1)])
        index_list[source_list[index]] += 1

    for index in range(1, len(index_list)):
        index_list[index] = index_list[index] + index_list[index - 1]

    res_list = [None for _ in range(0, len(source_list))]
    for index in range(len(source_list) - 1, -1, -1):
        element = source_list[index]
        res_list[index_list[element] - 1] = element
        index_list[element] -= 1

    source_list = res_list
    return source_list
