import unittest

from weather import report


class ReportTest(unittest.TestCase):
    def test_metric_report(self):
        self.assertEqual(report(68, 10), "20.0°C, wind 16.1 km/h")

    def test_freezing_point(self):
        self.assertEqual(report(32, 0), "0.0°C, wind 0.0 km/h")
