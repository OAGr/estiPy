from estimate import Estimate
from distribution import Distribution
import dependent.dependent

import pdb
class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution(*params)

    def run(self,n):
        return self.distribution.run(n)

    def buildDependent(self, operation, others):
        if len(others) == 1:
            return dependent.dependent.DependentEstimate(operation, self, *others)
        else:
            return dependent.dependent.DependentEstimate(operation, *([self] + others))


