__author__ = 'root'

import logging
from logging import Logger


LEVEL = "DEBUG"


class OVSconsolelogger(Logger, object):

    def __init__(self):
        Logger.__init__(self, "OVS-CONSOLE")
        # Create console handler
        console = logging.StreamHandler()

        # Add console handler to logging handler
        self.addHandler(console)

        # Setting Logging LEVEL
        self.setLevel(LEVEL)

logger = OVSconsolelogger()
