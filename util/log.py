__author__ = 'root'

from util import const
import logging

LEVEL = const.DEBUG_LEVEL
logger = logging.getLogger(const.LOG_NAME)
logger.setLevel(LEVEL)
console = logging.StreamHandler()
console.setLevel(LEVEL)
logger.addHandler(console)