from Refueling.fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/5") == 60
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(60) == "60%"
    assert gauge(50) == "50%"

def test_gaugeFull():
    assert gauge(99) == "F"

def test_gaugeEmpty():
    assert gauge(1) == "E"

def test_ZeroDivisionErrors():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_ValueErrors():
    with pytest.raises(ValueError):
        convert("cat/dog")

