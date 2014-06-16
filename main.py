from estipy.estimate import *
from estipy.distribution import *
from estipy.independent import *

import pdb

print 'test'

def testing():
    pdb.set_trace()
    print 'there'

I = IndependentEstimate
aaa = Estimate()
bbb =  Distribution(5,2)

dogs = IndependentEstimate(5,2)
#dogs.mean = 5, dogs.std = 2

cats = IndependentEstimate(1,1)
#cats.mean = 1, cats.std = 1

animals = dogs + cats
#animals.mean ~= 6
#animals.std ~= 3
#animals.run(3) = [4,6,5]

cats.mean = 10
#animals.mean ~= 11

insects = IndependentEstimate(100,3)

living_beings = animals + insects
#living_beings.mean = 100
pdb.set_trace()
print animals
pdb.set_trace()
wolves = dogs + 3

