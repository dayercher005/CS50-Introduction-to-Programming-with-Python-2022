from plates import is_valid

def test_alphabets():
    assert is_valid("50") == False
    assert is_valid("C1FJFL") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CCCCCCC") == False
    assert is_valid("CS") == True

def test_numberPlacement():
    assert is_valid("AAA222") == True
    assert is_valid("AA22AA") == False

def test_zeroPlacement():
    assert is_valid("AAAA10") == True
    assert is_valid("AAAA01") == False

def test_alphanumericCharacters():
    assert is_valid("PR.FH1") == False
