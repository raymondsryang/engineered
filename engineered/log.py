"""
Logging utilities
"""
import functools
import logging
import pickle
import traceback
from typing import Callable, Iterable, Mapping, Optional

from engineered import Picklable


def fn_record(logger,
              level: int = logging.INFO,
              label: Optional[str] = None,
              reraise: bool = True):
    """
    A decorator record the function input and output
    """

    # 入参为函数，这些函数的入参和出参都是Pickable的
    def decorator(func: Callable[..., Picklable]) -> Callable[..., Picklable]:

        @functools.wraps(func)
        def wrapper(*args: Iterable[Picklable], **kwargs: Mapping[str,
                                                                  Picklable]):
            error = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error = e

            logger.bind(
                args=pickle.dumps(args),
                kwargs=pickle.dumps(kwargs),
                result=pickle.dumps(result),
                error=error,
                tb=traceback.format_exc() if error is not None else None,
                label=label).log(level, "Record")

            if error is not None and reraise:
                raise error
            return result

        return wrapper

    return decorator
