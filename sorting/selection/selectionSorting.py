# -*- coding:utf-8 -*-
from sorting.utils import sorting, swapElements


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
        for j in range(i + 1, total_count):
            if source_list[j] < source_list[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            swapElements(source_list, i, smallest_index)
    return source_list
