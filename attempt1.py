# -*- coding: utf-8 -*-
from pylab import *
from scipy.stats import *
from random import *
from operator import *
from numpy import *
import pdb
class Distribution:
    def __init__(self, mean, stdev, dist = gauss):
        self.mean = mean
        self.stdev = stdev
        self.dist = dist

    def run(self, n = 1):
        return array([self.dist(self.mean, self.stdev) for _ in range(n)])
    def __str__(self):
        return "%d±%d with distribution %s" % (self.mean, self.stdev, self.dist.im_func.func_name)
    def __add__(self,other):
        if isinstance(other, int):
            return Distribution(self.mean + other, self.stdev, self.dist)
        #elif isinstance(other, Distribution):
        #    if other.dist == gauss and self.dist == gauss:
        #        return Distribution(self.mean + other.mean, self.stdev + other.stdev)
        return Combination('+', [self, other])

class Combination:

    def __init__(self, operation, *estimates):
        pdb.set_trace()
        operations = {"+":DisFunc.add, "*":DisFunc.multiply, "/":DisFunc.divide, '-':DisFunc.subtract}
        self.operation = operations[operation]
        self.estimates = estimates

    def run(self, n=1):
        generated = self.generate_n(n)
        return self.operation(generated)

    def generate_n(self):
        return [d.run(n) for d in estimates]

    def __add__(self,other):

    def __sub__(self,other):

    def __div__(self,other):


class DisFunc:
    def add(generated):
        return reduce(add, generated,1)

    def multiply(generated):
        return reduce(mul,generated, 1)

    def divide(generated):
        return reduce(div, generated[1:], generated[0])

    def subtract(generated):
        return reduce(sub, generated[1:], generated[0])



