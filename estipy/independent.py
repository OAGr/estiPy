from estimate import Estimate
from distribution import Distribution
import dependent.dependent as dp

class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution(*params)
    def __str__(self):
        return 'IndependentEstimate(' + str(self.distribution) + ')'
    def __repr__(self):
        #return "Est-Dist" + str(self.distribution)
        #return 'IndependentEstimate({0.distribution})'.format(self)
        return 'IndependentEstimate(' + str(self.distribution) + ')'

    def run(self,n):
        return self.distribution.run(n)

    def mean(self,n=0):
        return self.distribution.mean

    def std(self,n=0):
        return self.distribution.stdev

    def buildDependent(self, operation, others):
        if len(others) == 1:
            return dp.DependentEstimate(operation, self, *others)
        else:
            return dp.DependentEstimate(operation, *([self] + others))

Est = IndependentEstimate
