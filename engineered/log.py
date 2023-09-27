"""
Logging utilities
"""
import functools
import traceback
from typing import Any, Callable, Iterable, Mapping, Optional, Union


def fn_record(logger,
              level: Union[str, int] = "INFO",
              label: Optional[str] = None,
              reraise: bool = True,
              default_msg: Optional[str] = None):
    """
    A decorator record the function input and output
    """

    # 入参为函数，这些函数的入参和出参都是Pickable的
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args: Iterable[Any], **kwargs: Mapping[str, Any]):
            error = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error = e

            message = default_msg
            if message is None:
                message = f"Function {func.__name__} called"

            logger.bind(
                args=str(args),
                kwargs=str(kwargs),
                result=str(result),
                error=error,
                tb=traceback.format_exc() if error is not None else None,
                label=label).log(level, message)

            if error is not None and reraise:
                raise error
            return result

        return wrapper

    return decorator
