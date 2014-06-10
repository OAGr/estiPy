from estipy.independent import IndependentEstimate
from estipy.dependent.dependent import DependentEstimate, InputWrapper
import pdb
import unittest
import random
import numpy

class InputWrapperTest(unittest.TestCase):
    def setUp(self):
        self.ind_a = IndependentEstimate(5,3, random.Random(344).gauss)
        self.aint = 2
        self.afloat = 2.0

    def independent_estimate_runs_test(self):
        wrap1 = InputWrapper(self.ind_a)
        wrap1_run = wrap1.run(3)
        numpy.testing.assert_almost_equal(wrap1_run, [4.00630938,5.97782548,10.02321929])

    def int_runs_test(self):
        wrap2 = InputWrapper(self.aint)
        self.assertItemsEqual(wrap2.run(3), numpy.array([2,2,2]))

    def float_runs_test(self):
        wrap3 = InputWrapper(self.afloat)
        numpy.testing.assert_almost_equal(wrap3.run(3), numpy.array([2.0, 2.0, 2.0]))

    def rejects_bad_input_test(self):
        false1 = InputWrapper("don't work")
        self.assertFalse(false1.is_valid())
        false2 = InputWrapper(None)
        self.assertFalse(false2.is_valid())


class DependentTest(unittest.TestCase):
    def setUp(self):
        self.ind_a = IndependentEstimate(5,1, random.Random(344).gauss)
        self.ind_b = IndependentEstimate(10,100, random.Random(345).gauss)
        self.ints = [3,4]
        self.floats = [5.0,6.0]

    def rejects_bad_input_test(self):
        dep_a = DependentEstimate("+", None)
        dep_b = DependentEstimate("+", "badinput", 4)
        dep_c = DependentEstimate("+")
        for e in [dep_a, dep_b, dep_c]:
            self.assertFalse(e.valid_inputs())

    def runs_correctly_with_ints_test(self):
        dep = DependentEstimate('+', *self.ints)
        self.assertItemsEqual(dep.run(5), numpy.array([7,7,7,7,7]))

    def runs_correctly_with_floats_test(self):
        dep = DependentEstimate('+', *self.floats)
        self.assertItemsEqual(dep.run(5),
                numpy.array([11.0,11.0,11.0,11.0, 11.0]))

    def runs_with_all_inputs_test(self):
        inputs = [self.ind_a, self.ind_b]
        inputs += self.ints
        inputs += self.floats
        dep = DependentEstimate('+', *inputs)
        pdb.set_trace()
