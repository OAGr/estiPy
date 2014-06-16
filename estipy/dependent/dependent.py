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

    def __repr__(self):
        return '(' +  self.operation + ') => [' + ', '.join([str(e) for e in self.inputs]) + ']'

    def __str__(self):
        return '(' +  self.operation + ') => [' + ', '.join([str(e) for e in self.inputs]) + ']'

    def valid_inputs(self):
        return all([i.is_valid() for i in self.inputs]) and len(self.inputs)

    def run(self,n=1000):
        return mcsolver.run(self.operation, n, self.inputs)

    def buildDependent(self, operation, others):
        if len(others) == 1:
            return DependentEstimate(operation, self, *others)
        else:
            return DependentEstimate(operation, *([self] + others))


for stat in {'std','mean','median','average','var'}:
    def _find_stat(self, n=1000, stat=stat):
        return getattr(numpy, stat)(self.run(n))
    setattr(DependentEstimate, stat, _find_stat)

class InputWrapper(object):
    def __init__(self, baseObject):
        self.baseObject = baseObject
       
    def __str__(self):
        return self.baseObject.__str__()

    def run(self, n):
        if hasattr(self.baseObject, 'run'):
            return self.baseObject.run(n)
        elif self.is_num():
            return numpy.array([self.baseObject] * n)
        else:
            return numpy.array([None] * n)

    def is_none(self):
        return self.baseObject == None
    def is_num(self):
        return any([isinstance(self.baseObject, obj) for obj in [int,float,long]])
    def is_estimate(self):
        return isinstance(self.baseObject,
                estipy.independent.IndependentEstimate) or isinstance(self.baseObject, DependentEstimate)
    def has_distribution(self):
        return self.is_estimate() and hasattr(self.baseObject, 'distribution')
    def is_gaussian(self):
        return self.has_distribution() and self.baseObject.distribution.dist == random.gauss

    def is_valid(self):
        if self.is_none():
            return False
        else:
            return self.is_num() or self.is_estimate()


