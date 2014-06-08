from monte.distribution import Distribution
from monte.estimate import Estimate
import mcsolver
import numpy, random
import pdb

class DependentEstimate(Estimate):
    def __init__(self,operation, *inputs):
        self.operation = operation
        self.inputs = [InputWrapper(i) for i in inputs]

    def valid_inputs(self, inputs):
        return all([i.is_valid() for i in inputs])

    def run(self,n):
        return mcsolver.run(self.operation, self.inputs,n)

    def buildDependent(self, operation, *others):
        if len(others) == 1:
            return DependentEstimate(operation, self, others)
        else:
            return DependentEstimate(operation, *([self] + others))

class InputWrapper:
    def __init__(self, inp):
        self.inp = inp

    def run(self, n):
        if self.is_distribution():
            return self.inp.run(n)
        elif self.is_num():
            return numpy.array([self.inp] * n)
        else:
            return numpy.array([None] * n)

    def is_none(self):
        return self.inp == None
    def is_num(self):
        return any([isinstance(self.inp, obj) for obj in [int,float,long]])
    def is_distribution(self):
        return isinstance(self.inp, Distribution)
    def is_gaussian(self):
        return self.is_distribution() and self.inp.distribution.dist == random.gauss

    def is_valid(self):
        if self.is_none():
            return False
        else:
            return self.is_num() or self.is_distribution()


