import operator

def generate(operation, distributions, n):
    operations = {"+":add, "*":mul, "/":div, '-':sub}
    print 'hello'
    generated = [d.run(n) for d in distributions]
    operations[operation](generated)

def add(generated):
    print 'hello there'
    print reduce(operator.add, generated, 1)
    return reduce(operator.add, generated,1)

def mul(generated):
    return reduce(operator.mul,generated, 1)

def div(generated):
    return reduce(operator.div, generated[1:], generated[0])

def sub(generated):
    return reduce(operator.sub, generated[1:], generated[0])

