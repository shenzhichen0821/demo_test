# -*- coding:utf-8 -*-
import unittest
import os
import random
import datetime
import copy
from logger import logger

from sorting.bubble.bubbleSorting import bubbleSorting, bubbleUpgradeSorting
from sorting.selection.selectionSorting import selectionSorting
from sorting.insertion.insertionSorting import insertionSorting
from sorting.merge.mergeSorting import mergeSorting
from sorting.heap.heapSorting import heapSorting
from sorting.quick.quickSorting import quickSorting
from sorting.counting.countingSorting import countingStableSorting, countingUnstableSorting
from sorting.radix.radixSorting import radixSorting
from sorting.utils import getRandomList

_LIST_LENGTH = 1000
_UNIQUE_ELEMENT = False

_PRINT_STEP = 1000000
_DATA_FILE_PATH = "test.dat"
_USE_EXISTING_DATA = False


class SortingTest(unittest.TestCase):
    TEST_DATA = None

    def __init__(self, methodName='runTest'):
        super(SortingTest, self).__init__(methodName)
        if SortingTest.TEST_DATA is not None:
            return
        # prepare test data
        logger.info("Start to prepare test data.")
        if _UNIQUE_ELEMENT is True:
            self.__prepareUniqueList()
        else:
            self.__prepareDuplicateList()
        logger.info("Prepare test data end.")

        if _LIST_LENGTH < 50:
            logger.info("Origin list is:")
            logger.info("%s\n" % str(self.TEST_DATA))
        else:
            logger.info("Test data is too large to show. Length is %d\n" % _LIST_LENGTH)


    def __prepareDuplicateList(self):
        SortingTest.TEST_DATA = []
        if _USE_EXISTING_DATA is True:
            if not os.path.exists(_DATA_FILE_PATH):
                for i in range(0, _LIST_LENGTH):
                    if i % _PRINT_STEP == 0 and i != 0:
                        print(datetime.datetime.now(), "generated %d random digits..." % i)
                    SortingTest.TEST_DATA.append(random.randrange(start=0, stop=_LIST_LENGTH, step=1))

                with open(_DATA_FILE_PATH, 'w') as write_handler:
                    write_handler.write(str(SortingTest.TEST_DATA))
            else:
                with open(_DATA_FILE_PATH, "r") as read_handler:
                    SortingTest.TEST_DATA = eval(read_handler.read())
        else:
            for i in range(0, _LIST_LENGTH):
                if i % _PRINT_STEP == 0 and i != 0:
                    print(datetime.datetime.now(), "generated %d random digits..." % i)
                SortingTest.TEST_DATA.append(random.randrange(start=0, stop=_LIST_LENGTH, step=1))

    def __prepareUniqueList(self):
        SortingTest.TEST_DATA = getRandomList(_LIST_LENGTH)

    def setUp(self):
        pass

    def testDefault(self):
        from sorting.utils import sorting
        @sorting("default python sorting")
        def defaultSorting(source_list):
            return sorted(source_list)

        self.__assertTest(defaultSorting)

    def testBubble(self):
        self.__assertTest(bubbleSorting)

    def testBubbleUpgrade(self):
        self.__assertTest(bubbleUpgradeSorting)

    def testSelection(self):
        self.__assertTest(selectionSorting)

    def testInsertion(self):
        self.__assertTest(insertionSorting)

    def testMerge(self):
        self.__assertTest(mergeSorting)

    def testHeap(self):
        self.__assertTest(heapSorting)

    def testQuick(self):
        self.__assertTest(quickSorting)

    def testStableCounting(self):
        self.__assertTest(countingStableSorting)

    def testUnstableCounting(self):
        self.__assertTest(countingUnstableSorting)

    def testRadixCounting(self):
        self.__assertTest(radixSorting)

    def tearDown(self):
        pass

    def __assertTest(self, func):
        source = copy.copy(self.TEST_DATA)
        source = func(source)
        self.assertTrue(self.__isListSorted(source))

    def __isListSorted(self, ori_list):
        for i in range(0, len(ori_list) - 1):
            if ori_list[i] > ori_list[i + 1]:
                return False
        return True


if __name__ == "__main__":
    unittest.main()
