from random import randint
from unittest import TestCase
from datetime import datetime, timedelta
from plot.plot import plotFrequencyHistogram


class TestPlot(TestCase):

    def testPlotHistogram(self):
        testPoints = 1000
        start = datetime.now()

        datetimes = [
            start - timedelta(seconds=delta + randint(0, testPoints))
            for delta in range(testPoints)
        ]

        plotFrequencyHistogram(
            datetimes=datetimes,
            title="Test Graph",
            xLabel="datetimes",
            yLabel="frequencies",
        )
