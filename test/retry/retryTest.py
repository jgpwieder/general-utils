from time import time
from random import random
from unittest import TestCase
from retry.retryDecorator import retry


class TestCsvHelper(TestCase):

    def testReadAndWrite(self):
        start = time()
        while time() - start < 1:
            _mockError(failPercentage=0.999, start=start)


@retry(timeout=10, maxWait=0.5, limit=10)
def _mockError(failPercentage, start):
    print("DELTA: {}".format(time() - start))
    if random() < failPercentage:
        raise Exception("Mock Error")
