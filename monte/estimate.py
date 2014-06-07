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
        return self.getDependent('+', others)
    def sub(self,*others):
        return self.getDependent('-', others)
    def mul(self,*others):
        return self.getDependent('*', others)
    def div(self,*others):
        return self.getDependent('/', others)

    def buildDependent(self, operation, *others):
        pass


