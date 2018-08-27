# -*- coding:utf-8 -*-
from sorting.utils import sorting, swapElements


@sorting("insertion")
def insertionSorting(source_list):
    """
    插入排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    for i in range(1, total_count):
        insertIntoList(source_list, findIndex(source_list[0: i], source_list[i]), i, source_list[i])
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