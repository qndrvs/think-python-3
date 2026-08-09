## EXERCISES
import math

# 1. Ask a virtual assistant
print("\nEXERCISE 1")
def absolute_value_fixed(x: float) -> float:
    """
    Return the absolute value of x.

    Parameters
    ----------
    x : float
        The number to take the absolute value of.

    Returns
    -------
    float
        abs(x).
    """
    if x < 0:
        return -x
    return x  # covers x == 0 and x > 0

def absolute_value_extra_return(x: float) -> float:
    """
    Return the absolute value of x. Demonstrates a return statement that can never be reached (dead code).

    Parameters
    ----------
    x : float
        The number to take the absolute value of.

    Returns
    -------
    float
        abs(x).
    """
    if x < 0:
        return -x
    else:
        return x
    return 'This is dead code.'

def is_divisible(x: int, y: int) -> bool:
    """
    Check whether x is evenly divisible by y.

    Parameters
    ----------
    x : int
        The dividend.
    y : int
        The divisor. Must not be zero.

    Returns
    -------
    bool
        True if x is divisible by y, False otherwise.

    Raises
    ------
    ValueError
        If y is zero.
    """
    if y == 0:
        raise ValueError("The divisor cannot be zero.")
    return x % y == 0

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Compute the Euclidean distance between two points.

    Parameters
    ----------
    x1 : float
        X coordinate of the first point.
    y1 : float
        Y coordinate of the first point.
    x2 : float
        X coordinate of the second point.
    y2 : float
        Y coordinate of the second point.

    Returns
    -------
    float
        The distance between (x1, y1) and (x2, y2).
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("done\n")


# 2. Exercise
print("\nEXERCISE 2")
def hypot(a: float, b: float) -> float | None:
    """
    Compute the length of the hypotenuse of a right triangle given its two legs.

    Parameters
    ----------
    a : float
        Length of the first leg. Must be positive.
    b : float
        Length of the second leg. Must be positive.

    Returns
    -------
    float or None
        The hypotenuse length, or None if either leg is not positive.
    """
    if (a <= 0 or b <= 0): return
    return math.sqrt(pow(a, 2) + pow(b, 2))
print(hypot(3, 4) == 5.0)
print("done\n")


# 3. Exercise
print("\nEXERCISE 3")
def is_between(x: float, y: float, z: float) -> bool:
    """
    Check whether y lies strictly between x and z, in either direction.

    Parameters
    ----------
    x : float
        One bound.
    y : float
        The value to check.
    z : float
        The other bound.

    Returns
    -------
    bool
        True if y is strictly between x and z.
    """
    return (x < y < z) or (z < y < x)
print("done\n")


# 4. Exercise
print("\nEXERCISE 4")
def ackermann(m: int, n: int) -> int:
    """
    Compute the Ackermann function, a classic example of a recursive function that is not primitive recursive and grows extremely fast.

    Parameters
    ----------
    m : int
        Non-negative integer.
    n : int
        Non-negative integer.

    Returns
    -------
    int
        The value of the Ackermann function for (m, n).
    """
    if m == 0: return n+1
    if m > 0 and n == 0: return ackermann(m-1, 1)
    if m > 0 and n > 0: return ackermann(m-1, ackermann(m, n-1))
"""
print(ackermann(5, 5))
Error, because the number grows absurdly fast (this call is intractable in practice — it would take far too long / exceed the recursion limit).
"""
print("done\n")


# 5. Exercise
print("\nEXERCISE 5")
def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two integers using the Euclidean algorithm.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        The greatest common divisor of a and b.
    """
    if b == 0: return a
    return gcd(b, a % b)
print("done\n")