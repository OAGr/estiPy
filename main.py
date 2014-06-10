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
ccc = IndependentEstimate(5,2)
ddd = IndependentEstimate(1,1)

eee = ccc + ddd
fff = ccc + 5
print fff
pdb.set_trace()
