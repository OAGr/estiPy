from estimate import Estimate
from distribution import Distribution
import dependent.dependent as dp

class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution(*params)
        self.__dict__ = dict(self.__dict__.items() +
                self.distribution.__dict__.items())

    def run(self,n):
        return self.distribution.run(n)

    def buildDependent(self, operation, others):
        if len(others) == 1:
            return dp.DependentEstimate(operation, self, *others)
        else:
            return dp.DependentEstimate(operation, *([self] + others))

