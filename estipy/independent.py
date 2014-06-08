from estimate import Estimate
from distribution import Distribution
from dependent.dependent import DependentEstimate

import pdb
class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution(*params)

    def run(self,n):
        return self.distribution.run(n)

    def buildDependent(self, operation, others):
        if len(others) == 1:
            return DependentEstimate(operation, self, *others)
        else:
            return DependentEstimate(operation, *([self] + others))


