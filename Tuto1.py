#!/usr/bin/env python3

import functools
import logging
from typing import Union

class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        # create a file handler
        handler_file = logging.FileHandler("test_log.log")
        handler_file.setLevel(logging.DEBUG)

        # create stdout handler
        handler_stdout = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
        handler_stdout.setFormatter(formatter)
        handler_stdout.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
        handler_file.setFormatter(formatter)

        # add the file handler to the logger
        self.logger.addHandler(handler_file)
        self.logger.addHandler(handler_stdout)
        

    def get_logger(self, name=None):
        return logging.getLogger(name)

def get_default_logger():
    return MyLogger().get_logger()

def log(_func=None, *, my_logger: MyLogger = None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if my_logger is None:
                logger = MyLogger().logger
            else:
                if isinstance(my_logger, MyLogger):
                    logger = my_logger.logger
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logger.debug(f"function {func.__name__} called with args {signature}")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
                raise e
            logger.info(f"Function {func.__name__} return with {result}")
            return result
        return wrapper

    if _func is None:
        return decorator_log
    else:
        return decorator_log(_func)

@log(my_logger=MyLogger())
def sum(a, b=10):
    return a + b

sum(10 , b=5)