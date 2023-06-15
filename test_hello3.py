from hello3 import hello



def test_default():
    assert hello() == "hello, world"


def test_argument():
    #assert hello("David") == "hello, David"
    for name in ["Hermione","Harry","Ron"]:
        assert hello(name)==f"hello, {name}"
    
