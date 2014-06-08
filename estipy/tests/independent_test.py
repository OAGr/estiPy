from estipy.independent import IndependentEstimate
import pdb
import unittest
import random
import numpy

class EstimateTest(unittest.TestCase):
    def setUp(self):
        self.est = IndependentEstimate(5,3, random.Random(344).gauss)

    def test_distribution(self):
        dist = self.est.distribution
        self.assertEqual(self.est.distribution.__class__.__name__, 'Distribution')
        self.assertEqual(dist.mean, 5)
        self.assertEqual(dist.stdev, 3)

    def test_run(self):
        run = self.est.run(5)
        self.assertEqual(run.__class__, numpy.ndarray)
        self.assertEqual(len(run), 5)
        self.assertAlmostEqual(run[0], 4.0063093788)

    def test_create_from(self):
        aa = self.est + 4
        self.assertEqual(aa.__class__.__name__, 'DependentEstimate')

