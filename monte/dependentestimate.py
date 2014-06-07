import mcgen
from estimate import Estimate
from distribution import Distribution
from analyticsolver import AnalyticSolver

class DependentEstimate(Estimate):
    def __init__(self,operation, *estimates):
        self.operation, self.estimates = estimates, estimates

    def run(self,n):
        if self.distribution:
            return self.distribution.run(n)
        else:
            return mcgen.run(self.operation, self.estimates,n)

    @property
    def distribution(self):
        distribution = AnalyticSolver.find_distribution(self.operation, self.estimates)
        self.distribution = distribution
        return self.distribution

    def buildDependent(self, operation, *others):
        if len(others) == 1:
            return DependentEstimate(operation, self, others)
        else:
            return DependentEstimate(operation, *([self] + others))





