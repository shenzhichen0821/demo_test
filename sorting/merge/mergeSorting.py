# -*- coding:utf-8 -*-
from sorting.utils import sorting


@sorting("merge")
def mergeSorting(source_list):
    """
    归并排序
    :param source_list:
    :return:
    """
    return divide(source_list)

def divide(source_list):
    length = len(source_list)
    if length == 1:
        return source_list

    first_half = divide(source_list[0: int(length / 2)])
    second_half = divide(source_list[int(length / 2):])
    return mergeTwoHalf(first_half, second_half)

def mergeTwoHalf(first_half, second_half):
    buffer_list = []
    while len(first_half) != 0 and len(second_half) != 0:
        buffer_list.append(first_half.pop(0) if first_half[0] <= second_half[0] else second_half.pop(0))
    if len(first_half) != 0:
        buffer_list.extend(first_half)
    if len(second_half) != 0:
        buffer_list.extend(second_half)
    return buffer_list

