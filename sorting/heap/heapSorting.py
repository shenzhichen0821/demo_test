# -*- coding:utf-8 -*-
import heapq
from sorting.utils import sorting


@sorting("heap")
def heapSorting(source_list):
    """
    堆排序
    :param source_list:
    :return:
    """
    total_count = len(source_list)
    buffer_list = []
    heapq.heapify(source_list)
    for _ in range(total_count):
        buffer_list.append(heapq.heappop(source_list))
    source_list = buffer_list
    return source_list

# @sorting("heap")
# def heapSorting(source_list):
#     """
#     堆排序
#     :param source_list:
#     :return:
#     """
#     total_count = len(source_list)
#     buffer_list = []
#     for index in range(0, total_count - 1):
#         heapify(source_list)
#         current_length = len(source_list)
#         swapElements(source_list, 0, current_length - 1)
#         buffer_list.insert(0, source_list.pop(current_length - 1))
#     source_list.extend(buffer_list)
#     return source_list
#
#
# def heapify(heap_list):
#     length = len(heap_list)
#     last_root_index = int(length / 2 - 1)
#     for i in range(last_root_index, -1, -1):
#         if justify(heap_list, i) is True:
#             break
#     else:
#         return
#     heapify(heap_list)
#
#
# def justify(heap_list, root_index):
#     left = (2 * root_index + 1)
#     right = (2 * root_index + 2)
#     try:
#         bigger_leaf = left if heap_list[left] > heap_list[right] else right
#     except:
#         bigger_leaf = left
#
#     if heap_list[bigger_leaf] > heap_list[root_index]:
#         swapElements(heap_list, bigger_leaf, root_index)
#         return True
#     else:
#         return False
