def cat(x, y):
    return x + y

def dog(x, y):
    return x ** y

def test_cat():
    assert cat(5, 15) == 20
    assert cat('hello', 'world') == 'helloworld'

def test_dog():
    assert dog(2, 3) == 8
    assert dog(1918, 0) == 1