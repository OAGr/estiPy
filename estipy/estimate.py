import numpy

class Estimate:
    def __add__(self,other):
        return self.add(other)
    def __sub__(self,other):
        return self.sub(other)
    def __mul__(self,other):
        return self.mul(other)
    def __div__(self,other):
        return self.div(other)

    def add(self,*others):
        return self.buildDependent('+', others)
    def sub(self,*others):
        return self.buildDependent('-', others)
    def mul(self,*others):
        return self.buildDependent('*', others)
    def div(self,*others):
        return self.buildDependent('/', others)

    def buildDependent(self, operation, *others):
        class DependentMock:
            def __init__(self,operation, others):
                self.operation = operation
                self.others = others
        return DependentMock(operation, *others)

    def stats(self, n=1000):
        mean = self.mean(n)
        std = self.std(n)
        median = self.median(n)
        return "mean:" + str(mean) + ",std:"+ str(std) + ",med: " +str(median)

for stat in {'std','mean','median','average','var'}:
    def _find_stat(self, n=1000, stat=stat):
        return getattr(numpy, stat)(self.run(n))
    setattr(Estimate, stat, _find_stat)


