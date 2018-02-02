from nose.tools import raises


@raises(AssertionError)
def test_this_throws_an_exception():
    assert False, "THrowing exceptions"

