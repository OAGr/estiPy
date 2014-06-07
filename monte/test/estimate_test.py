import estimate

def test_b():
    assert 'c' == 'c'

class IndependentTests:
    def test_create(self):
        a = Estimate()
        assert a.__class__ == Estimate
