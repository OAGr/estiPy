from ..distribution import Distribution

def test_Distribution():
    a = Distribution(5,2)
    assert a.__class__ == Distribution
    assert a.mean == 5
    assert a.stdev == 2
    assert len(a.run(10)) == 10

