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

    def update_distribution(self):
        distribution = AnalyticSolver.find_distribution(self.operation, self.estimates)
        self.distribution = distribution
        return distribution

    @property
    def distribution(self):
        self.update_distribution()
        return self.distribution



