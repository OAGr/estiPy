import numpy, random

class Distribution:
    def __init__(self, mean, stdev, dist = random.gauss):
        self.mean = mean
        self.stdev = stdev
        self.dist = dist

    def run(self, n=1):
        return numpy.array([self.dist(self.mean, self.stdev) for _ in range(n)])

   # def __str__(self):
   #     return "%d%d with distribution %s" % (self.mean, self.stdev, self.dist.im_func.func_name)


