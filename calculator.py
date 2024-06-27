def sum(x, y):
    """Sum x and y

    >>> sum (10, 20)
    30
    >>> sum (-10, 20)
    10
    >>> sum (1.5, 2.5)
    4.0
    >>> sum ('10', 2.5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float.
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float.'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float.'
    return x + y


def subtraction(x, y):
    """Subtraction x and y

    >>> subtraction(20, 10)
    10
    >>> subtraction(-20, 10)
    -30
    >>> subtraction(-20, -10)
    -10
    >>> subtraction('20', 10)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float.
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float.'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float.'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
