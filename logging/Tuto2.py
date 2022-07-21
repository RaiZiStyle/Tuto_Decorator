#!/usr/bin/env python3

import logging
import functools
class LogDecorator(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        formatter = "[%(asctime)s - %(name)s - %(levelname)s] %(message)s"
        rt = logging.basicConfig(level=logging.DEBUG,
                                format=formatter,
                                handlers=[logging.StreamHandler()])
        # create a file handler
        handler_file = logging.FileHandler("test_log.log")
        handler_file.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
        handler_file.setFormatter(formatter)

        # add the file handler to the logger
        self.logger.addHandler(handler_file)

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.critical("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                self.logger.error("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                self.logger.warning("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                self.logger.info("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                self.logger.debug("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                result = fn(*args, **kwargs)
                return result
            except Exception as ex:
                self.logger.warning("Exception {0}".format(ex))
                raise ex
            return result
        return decorated

@LogDecorator()
def sum(a, b, c):
    return a + b + c


sum(1,2,3)
    
