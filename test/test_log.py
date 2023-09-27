"""
"""
import logging
import unittest
from contextlib import contextmanager
from typing import Dict

from loguru import logger

from engineered.log import fn_record


@contextmanager
def capture_logs(level=logging.INFO, format="{extra}"):
    """
    Capture loguru-based logs for testing.
    See Detail: https://github.com/Delgan/loguru/issues/616#issuecomment-1068364919
    """
    output = []
    handler_id = logger.add(output.append, level=level, format=format)
    yield output
    logger.remove(handler_id)


class TestLog(unittest.TestCase):

    def test_extra_record(self):

        with capture_logs() as caplog:  # capture loguru log, and assert it

            @fn_record(logger=logger, level=logging.INFO)
            def add(a, b):
                return a + b

            _ = add(1, 2)

        self.assertEqual(len(caplog), 1)
        extra: Dict = caplog[0].record["extra"]
        keys = extra.keys()
        self.assertListEqual(list(keys), [
            "args",
            "kwargs",
            "result",
            "error",
            "tb",
            "label",
        ])
