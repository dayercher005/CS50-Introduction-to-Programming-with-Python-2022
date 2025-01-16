from Testing_my_twttr.twttr import shorten

def test_punctuation():
    assert shorten("cat!!!") == "ct!!!"

def test_uppercase():
    assert shorten("CAT") == "CT"

def test_lowercase():
    assert shorten("cat") == "ct"

def test_numbers():
    assert shorten("1cat") == "1ct"
