from ..estimate import Estimate
import unittest

class TestTest(unittest.TestCase):
    def test_thing1(self):
        self.assertEqual(5,5)

def test_b():
    a = Estimate()
    assert a.__class__ == Estimate

class IndependentTests:
    def test_create(self):
        a = Estimate()
        assert a.__class__ == Estimate
        assert a.__class__ == Estimate

#if __name__ == "__main__":
#    print 'hi'
