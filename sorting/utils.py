# -*- coding:utf-8 -*-
import datetime
from logger import logger


def sorting(func_name):
    def wrapper(cls):
        def _(*args, **kwargs):
            logger.debug("Sorting starts!!!")
            start = datetime.datetime.now()
            res = cls(*args, **kwargs)
            end = datetime.datetime.now()
            logger.debug("Sorting ends!!!")
            delta = (end - start).total_seconds()
            logger.info("[%s] Total time cost is: %f seconds\n" % (func_name, delta))
            return res
        return _
    return wrapper


def swapElements(source_list, i, j):
    """
    swap elements in list
    :param source_list:
    :param i:
    :param j:
    :return:
    """
    buffer_i = source_list[i]
    source_list[i] = source_list[j]
    source_list[j] = buffer_i
