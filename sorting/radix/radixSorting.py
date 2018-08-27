# -*- coding:utf-8 -*-
from sorting.utils import sorting


@sorting("radix")
def radixSorting(source_list):
    """
    基数排序
    :param source_list:
    :return:
    """
    for dest in range(1, len(str(len(source_list))) + 1):
        source_list = countingSortingByElement(source_list, dest)
    return source_list

def countingSortingByElement(source_list, dest):
    """
    根据某一位对序列进行排序
    :param source_list:
    :return:
    """
    index_list = [0 for _ in range(10)]
    for index in range(0, len(source_list)):
        element = str(source_list[index])
        try:
            index_list[int(element[-dest])] += 1
        except:
            index_list[0] += 1

    for index in range(1, len(index_list)):
        index_list[index] = index_list[index] + index_list[index - 1]

    res_list = [None for _ in range(0, len(source_list))]
    for index in range(len(source_list) - 1, -1, -1):
        element = str(source_list[index])
        try:
            source_index = int(element[-dest])
        except:
            source_index = 0
        res_list[index_list[source_index] - 1] = int(element)
        index_list[source_index] -= 1

    source_list = res_list
    return source_list
