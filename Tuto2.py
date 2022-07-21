#!/usr/bin/env python3

import logging
import functools
class LogDecorator(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
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
    
