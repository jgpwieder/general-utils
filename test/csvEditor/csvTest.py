from unittest import TestCase
from file.csvEditor import readCsv, writeCsv

_testFile = "testCsv.csv"
_testOutputFile = "testCsvOutput.csv"


class TestCsvHelper(TestCase):

    def testReadAndWrite(self):
        fileData = readCsv(_testFile)
        writeCsv(fileName=_testOutputFile, data=fileData)
        newFileData = readCsv(_testOutputFile)
        if newFileData != fileData:
            raise Exception
