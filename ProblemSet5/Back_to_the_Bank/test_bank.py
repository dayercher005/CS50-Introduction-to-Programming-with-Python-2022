from ProblemSet5.Back_to_the_Bank.bank import value

def test_lowercase():
    assert value("hello") == 0

def test_uppercase():
    assert value("HELLO") == 0

def test_phrase():
    assert value("Hello, Tom!") == 0
