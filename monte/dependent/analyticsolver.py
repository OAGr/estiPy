''' Takes in a set of estimates.  Finds if an analytical solution
exists.  If it does, finds the analytical solution.
'''
class Solution:
    def __init__(self,operation, *inputs):
        self.operation = operation
        self.inputs = InputSet(inputs)

    def exists(self):
        return self.distributions.are_gaussians or self.distributions.are_numbers

    def find(self):
        if not self.exists():
            return None
        else:
            return 6
        #operations = {"+":_add, "*":_mul, "/":_div, '-':_sub}
        #return operations[self.operation](self.distributions)

    def gaussian_find(self):
        #TODO: Figure this out
#        inputs[0].add(inputs[1:])
        #def _add(inputs):
            #mean = sum([i.mean for i in inputs])
            #stdev = reduce(operator.add, [i.stdev for i in inputs], 1)

        #operations = {"+":_add, "*":_mul, "/":_div, '-':_sub}
        #return operations[self.operation](self.distributions)
        pass


class InputSet:
    def __init__(self,*inputs):
        self.inputs = inputs

    def contains_unanalytic(self):
        return None in self.inputs

    def are_gaussians(self):
        all([e.is_gaussian() for e in self.inputs])

    def are_numbers(self):
        all([e.is_num() for e in self.inputs])

