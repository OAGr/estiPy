import operator

def run(operation, estimates, n):
    operations = {"+":add, "*":mul, "/":div, '-':sub}
    generated = [d.run(n) for d in estimates]
    return operations[operation](generated)

def add(generated):
    return reduce(operator.add, generated,1)

def mul(generated):
    return reduce(operator.mul,generated, 1)

def div(generated):
    return reduce(operator.div, generated[1:], generated[0])

def sub(generated):
    return reduce(operator.sub, generated[1:], generated[0])

