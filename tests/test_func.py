def cat(x, y):
    return x + y

def dog(x, y):
    return x ** y

def woof(a):
    return "woof"

def meow(a, b, c):
    return "meow" if (a + b + c) > 0 else "bark"

def test_cat():
    assert cat(5, 15) == 20
    assert cat("hello", "world") == "helloworld"
    assert cat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_dog():
    assert dog(2, 3) == 8
    assert dog(1918, 0) == 1
    assert dog(9, 2) == 81

def test_woof():
    assert woof(1239) == "woof"
    assert woof("hello world") == "woof"

def test_meow():
    assert meow(-1, 9, -8) == "bark"
    assert meow(-9, -12, -4) == "bark"
    assert meow(0, 0, 183) == "meow"