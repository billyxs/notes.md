# https://www.pythonmorsels.com/exercises/ad57c49f8a0042729e347cc34e8ac0e6/

from math import sqrt 
from decimal import Context, Decimal, localcontext
import cmath


def is_perfect_square_(num, *, complex=False):
    if num < 0:
        return False

    return sqrt(num).is_integer()


# Solution

def is_perfect_square_1(number):
    """Return True if given number is the square of an integer."""
    return int(sqrt(number))**2 == number


def is_perfect_square_2(number):
    """Return True if given number is the square of an integer."""
    return int(sqrt(number)) == sqrt(number)


def is_perfect_square_3(number):
    """Return True if given number is the square of an integer."""
    return sqrt(number) % 1 == 0


def is_perfect_square_4(number):
    """Return True if given number is the square of an integer."""
    return sqrt(number).is_integer()


def is_perfect_square_5(number):
    """Return True if given number is the square of an integer."""
    return sqrt(number).is_integer()


# Bonus 1

def is_perfect_square_6(number):
    """Return True if given number is the square of an integer."""
    try:
        return sqrt(number).is_integer()
    except ValueError:
        return False

# Bonus 2


def is_perfect_square_7(number):
    """Return True if given number is the square of an integer."""
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number

# Bonus 3 - Complex numbers


def is_perfect_square(number, *, complex=False):
    """Return True if given number is the square of an integer."""
    if complex:
        root = cmath.sqrt(number)
        return root.real.is_integer() and root.imag.is_integer()
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number
