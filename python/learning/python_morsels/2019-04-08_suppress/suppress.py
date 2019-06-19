# https://www.pythonmorsels.com/exercises/ded322173d47424581be45adaeeca90d/

# creating our own contextlib.suppress function

# Articles
# http://book.pythontips.com/en/latest/context_managers.html
# https://realpython.com/primer-on-python-decorators/#simple-decorators
# https://www.geeksforgeeks.org/class-as-decorator-in-python/


import sys
from contextlib import contextmanager, ContextDecorator

from dataclasses import dataclass
from types import TracebackType
from typing import Optional

from functools import wraps

class suppress_():

    """Context manager to suppress list of errors"""

    def __init__(self, *args):
        self.types = args

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception, traceback):
        self.traceback = traceback
        self.exception = exception
        if exception_type in self.types:
            return True
        return False


# Solutions

class suppress_1:

    """Context manager that suppresses exceptions of given type"""

    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception, traceback):
        # return isinstance(exception, exception_type)
        return exception and issubclass(exception, self.exception_type)


@contextmanager
def suppress_2(exception_type):
    try:
        yield
    except exception_type:
        pass


# Bonus 1 - accept any number of exceptions

class suppress_3:

    """Context manager that suppresses exceptions of given type"""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception, traceback):
        return isinstance(exception, self.exception_types)


# Bonus 2 - support context "with as" 

# Basic exception class
class ExceptionInfo_1:
    exception = None
    traceback = None

# Typed exception class
@dataclass
class ExceptionInfo:
    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None

@contextmanager
def suppress_4(*exception_types):
    """Context manager that suppresses exceptions of given type"""
    info = ExceptionInfo()
    
    try:
        yield info
    except exception_types as e:
        info.exception = e 
        info.traceback = e.__traceback__



class suppress_5:

    """Context manager that suppresses exceptions of given type"""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exception_types)


# Bonus 3 - make context manager work as a decorator

class suppress_6(ContextDecorator):

    """Context manager that suppresses exceptions of given type"""

    def __init__(self, *exception_types, default=None):
        self.exception_types = exception_types
        self.default = None

    # Replaced by ContextDecorator
    """
    def __call__(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            with self:
                return function(*args, **kwargs)
        return wrapper
    """

    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exception_types)


# ExceptionInfo declared for example above
@contextmanager
def suppress(*exception_types):
    """Context manager that suppresses exceptions of given type"""
    info = ExceptionInfo()
    try:
        yield info
    except exception_types as e:
        info.exception = e
        info.traceback = e.__traceback__



