import operator

'''
If no analytical solution exists, this is here to run a monte carlo
simulation on a given set of estimations with a given operator.

Receives a set of estimates, an operation, and n, a number of runs to
make.  Outputs the resulting set of runs.

Example Input: 
run("*", 5, IndependentEstimate(5,2), IndependentEstimate(7,3)
IndependentEstimate(10,3))

Example Output:
[360,301,297,271,389]
'''
import pdb
def run(operation, n, estimates):
    operations = {"+":_add, "*":_mul, "/":_div, '-':_sub}
    generated = [d.run(n) for d in estimates]
    return operations[operation](generated)

def _add(generated):
    return reduce(operator.add, generated,0)

def _mul(generated):
    return reduce(operator.mul,generated, 1)

def _div(generated):
    return reduce(operator.div, generated[1:], generated[0])

def _sub(generated):
    return reduce(operator.sub, generated[1:], generated[0])

