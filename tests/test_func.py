def cat(x, y):
    return x + y

def dog(x, y):
    return x ** y

def test_cat():
    assert cat(5, 15) == 20
    assert cat('hello', 'world') == 'helloworld'
    assert cat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_dog():
    assert dog(2, 3) == 8
    assert dog(1918, 0) == 1
    assert dog(9, 2) == 81