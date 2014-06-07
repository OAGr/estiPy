from ..estimate import Estimate

def test_b():
    a = Estimate()
    assert a.__class__ == Estimate

class IndependentTests:
    def test_create(self):
        a = Estimate()
        assert a.__class__ == Estimate
        assert a.__class__ == Estimate

#if __name__ == "__main__":
#    print 'hi'
