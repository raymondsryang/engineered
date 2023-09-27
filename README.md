# engineered
Python tools for engineering




# Usage

## Logging tools

fn_record: record the function call and return value, when we call third-party function, we can use this tool to record the function call and return value, then we can use the log to debug the code.

Output format based on logger configuration, but loguru message will contains filds below:
- args: the args of the function
- kwargs: the kwargs of the function
- result: the return value of the function
- error: the exception message string if the function raise exception
- tb: the traceback of the exception if the function raise exception
- label: the label of the function


```python
from engineered import fn_record
from loguru import logger

logger.add(sys.stdout, serialize=True, format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}")

# Usage
@fn_record(logger=logger)
def add(a, b):
    return a + b

_ = add(1, 2)
```

and output will be like this:

```json
{
    "text": "2023-09-27 13:02:13 INFO Function add called\n",
    "record": {
        "elapsed": {
            "repr": "0:00:00.334439",
            "seconds": 0.334439
        },
        "exception": null,
        "extra": {
            "args": "(1, 2)",
            "kwargs": "{}",
            "result": "3",
            "error": null,
            "tb": null,
            "label": null
        },
        "file": {
            "name": "log.py",
            "path": "/xxx/xxx/xxx/log.py"
        },
        "function": "wrapper",
        "level": {
            "icon": "ℹ️",
            "name": "INFO",
            "no": 20
        },
        "line": 34,
        "message": "Function add called",
        "module": "log",
        "name": "engineered.log",
        "process": {
            "id": 272773,
            "name": "MainProcess"
        },
        "thread": {
            "id": 139810909099840,
            "name": "MainThread"
        },
        "time": {
            "repr": "2023-09-27 13:02:13.875729+08:00",
            "timestamp": 1695790933.875729
        }
    }
}
```

