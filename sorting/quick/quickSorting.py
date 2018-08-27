# -*- coding:utf-8 -*-
from sorting.utils import sorting


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
        if ori_list[index] <= ori_list[end_index]:
            ori_list.insert(tail_index, ori_list.pop(index))
            tail_index += 1
    ori_list.insert(tail_index, ori_list.pop(end_index))

    recursiveDivide(ori_list, start_index, tail_index - 1)
    recursiveDivide(ori_list, tail_index + 1, end_index)
