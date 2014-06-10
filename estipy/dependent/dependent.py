from estipy.distribution import Distribution
from estipy.estimate import Estimate
import estipy.independent
import mcsolver
import numpy, random
import pdb

class DependentEstimate(Estimate):
    def __init__(self,operation, *inputs):
        self.operation = operation
        self.inputs = [InputWrapper(i) for i in inputs]

    def valid_inputs(self):
        return all([i.is_valid() for i in self.inputs]) and len(self.inputs)

    def run(self,n=1000):
        return mcsolver.run(self.operation, n, self.inputs)

    def avg(self,n):
        return sum(self.run(n)) / n

    def std(self,n=1000):
        return numpy.std(self.run(n))

    def mean(self,n=1000):
        return numpy.mean(self.run(n))

    def var(self,n=1000):
        return numpy.var(self.run(n))

    def buildDependent(self, operation, *others):
        if len(others) == 1:
            return DependentEstimate(operation, self, others)
        else:
            return DependentEstimate(operation, *([self] + others))

class InputWrapper:
    def __init__(self, inp):
        self.inp = inp

    def run(self, n):
        if self.is_estimate() or self.has_distribution():
            return self.inp.run(n)
        elif self.is_num():
            return numpy.array([self.inp] * n)
        else:
            return numpy.array([None] * n)

    def is_none(self):
        return self.inp == None
    def is_num(self):
        return any([isinstance(self.inp, obj) for obj in [int,float,long]])
    def is_estimate(self):
        return isinstance(self.inp,
                estipy.independent.IndependentEstimate) or isinstance(self.inp, DependentEstimate)
    def has_distribution(self):
        return self.is_estimate() and hasattr(self.inp, 'distribution')
    def is_gaussian(self):
        return self.has_distribution() and self.inp.distribution.dist == random.gauss

    def is_valid(self):
        if self.is_none():
            return False
        else:
            return self.is_num() or self.is_estimate()


