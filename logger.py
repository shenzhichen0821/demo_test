# -*- coding:utf-8 -*-
import logging
import sys


logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

# file_handler = logging.FileHandler("test.log")
# file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

# logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)
