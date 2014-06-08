from monte.distribution import *
import unittest

def test_Distribution():
    a = Distribution(5,2)
    assert a.__class__ == Distribution
    assert a.mean == 5
    assert a.stdev == 2
    assert len(a.run(10)) == 10

class DistributionTest(unittest.TestCase):
    def setUp(self):
        self.dis = Distribution(5,3)
        self.alt = Distribution(5,3, random.Random(61).gauss)

    def test_mean(self):
        self.assertEqual(self.dis.mean, 5)

    def test_stdev(self):
        self.assertEqual(self.dis.stdev, 3)

    def test_dist(self):
        self.assertEqual(self.dis.dist, random.gauss)

    def test_run(self):
        self.assertAlmostEqual(self.alt.run(1)[0], 1.17570161)
        self.assertEqual(len(self.alt.run(10)), 10)
        self.assertAlmostEqual( sum(self.alt.run(100))/100, 4.6980737499)
