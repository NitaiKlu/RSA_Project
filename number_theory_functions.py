from random import randrange
import numpy
import math

from numpy import long

small_power = 2
def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if (a<b):
        return extended_gcd(b,a)
    if(b==0):
        return (a, 1, 0)
    (gcd, x, y) = extended_gcd(a%b, b)
    #gcd = 1, x = 1, y = -2, a = 3, b = 1
    x1 = y #-2
    y1 = x - y * (a//b) #7
    return (gcd, x1, y1)




def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    (gcd, x, inverse) = extended_gcd(a,n)
    if(gcd != 1):
        return 0
    return inverse%n

def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    base = long(a)
    power = long(d)
    new_base = pow(base, small_power, n)
    if (power % small_power == 0):
        additional = 1
    else:
        additional = pow(base, power % small_power, n)
    new_power = power // small_power
    if(new_power <= 1):
        return (pow(new_base, 1, n) * additional)%n
    return (modular_exponent(new_base, new_power, n) * additional) %n

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None

