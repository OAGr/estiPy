from distribution import Distribution
from estimate import Estimate

class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution.new(params)

    def run(self,n):
        return self.distribution.run(n)
