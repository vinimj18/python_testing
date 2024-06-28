"""
1 - Receive an integer number
2 - Verify if the number is a multiple of 3 or 5:
    bacon and eggs
3 - Verify if the number is NOT a multiple of 3 nor 5:
    you starved
4 - Verify if the number is only a multiple of 3:
    bacon
5 - Verify if the number is only a multiple of 5:
    eggs
"""


def bacon_and_eggs(n):
    assert isinstance(n, int), 'n must be an int.'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon and eggs'
    if n % 3 == 0:
        return 'bacon'
    if n % 5 == 0:
        return 'eggs'
    return 'you starved'
