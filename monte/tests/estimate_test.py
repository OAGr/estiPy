from monte.estimate import *
from monte.dependent.dependent import *
import unittest

class TestTest(unittest.TestCase):
    def setUp(self):
        self.a = Estimate()
        self.b = Estimate()
        self.c = Estimate()

    def test_reg_add(self):
        dd = self.a + self.b
        self.assertEqual(dd.operation, '+')
        self.assertEqual(dd.others, (self.b,))

    def test_reg_mul(self):
        dd = self.a * self.b
        self.assertEqual(dd.operation, '*')
        self.assertEqual(dd.others, (self.b,))

    def test_alt_add(self):
        dd = self.a.add(self.b,self.c)
        self.assertEqual(dd.operation, '+')
        self.assertEqual(dd.others, (self.b,self.c))

    def test_alt_mult(self):
        dd = self.a.mul(self.b,self.c)
        self.assertEqual(dd.operation, '*')
        self.assertEqual(dd.others, (self.b,self.c))
