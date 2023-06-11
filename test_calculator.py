
"""def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")"""
import pytest
from calculator2 import square
def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0



