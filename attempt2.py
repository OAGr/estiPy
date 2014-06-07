import numpy
import random
import MonteCarloGenerator

class Distribution:
    def __init__(self, mean, stdev, dist = random.gauss):
        self.mean = mean
        self.stdev = stdev
        self.dist = dist

    def run(self, n=1):
        return numpy.array([self.dist(self.mean, self.stdev) for _ in range(n)])

   # def __str__(self):
   #     return "%d%d with distribution %s" % (self.mean, self.stdev, self.dist.im_func.func_name)


class Estimate:
    def run5(self,n):
        return 5

class IndependentEstimate(Estimate):
    def __init__(self,*params):
        self.distribution = Distribution.new(params)

class DependentEstimate(Estimate):
    def __init__(self,operation, *estimates):
        self.operation, self.estimates = estimates, estimates
        self.update_distribution()

    def run(self,n):
        if self.get_distribution():
            return self.distribution.run(n)
        else:
            return MonteCarloGenerator.run(self.operation, self.estimates,n)

    def update_distribution(self):
        distribution = AnalyticSolver.find_distribution(self.operation, self.estimates)
        self.distribution = distribution
        return distribution

    @property
    def distribution(self):
        self.update_distribution()
        return self.distribution

class AnalyticSolver:
    def find_distribution(self,operation, distributions):
        operations = {"+":self.add, "*":self.mul, "/":self.div, '-':self.sub}
        return operation[operations](distributions)

    def has_analytical_solution(operation, distributions):

        def all_are_nums_or_gaussian(distributions):
            def is_num(dis):
                return isinstance(dis, int) or isinstance(dis,float) or isinstance(dis,long)
            def is_gaussian(dis):
                return isinstance(dis, Distribution) and dis.dist == random.gauss
            return all([is_num(d) or is_gaussian(d) for d in distributions])
        return all_are_nums_or_gaussian(distributions)


