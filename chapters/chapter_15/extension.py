## EXTENSIONS
import math

# 1. Extension 1 - Operator overloading and the numeric protocol
"""
a. Build a class called Fraction representing an exact rational number p/q.
   __init__(self, numerator, denominator):
   - Raise ValueError if denominator == 0
   - Store in reduced form: divide both by gcd(abs(numerator), abs(denominator))
   - Ensure the denominator is always positive (move sign to numerator)
   Use math.gcd.
b. Implement these dunder methods:
   - __str__: returns 'p/q' (or just 'p' if q == 1)
   - __repr__: returns 'Fraction(p, q)'
   - __add__(self, other): supports Fraction + Fraction and Fraction + int
   - __radd__(self, other): supports int + Fraction
   - __sub__, __rsub__: subtraction
   - __mul__, __rmul__: multiplication
   - __truediv__, __rtruediv__: division (returns a Fraction)
   - __neg__: unary minus, returns -Fraction
   - __abs__: returns abs(Fraction)
   - __eq__: equality (compare reduced p and q)
   - __lt__, __le__, __gt__, __ge__: comparison (cross-multiply to compare)
   - __float__: returns float(numerator / denominator)
c. Write a function called farey_sequence(n) that returns the list of all Fraction objects p/q where 0 <= p/q <= 1 and 1 <= q <= n, sorted in ascending order.
   The Farey sequence F_5 starts: 0/1, 1/5, 1/4, 1/3, 2/5, 1/2, ...
   Use your comparison operators. Verify: len(farey_sequence(5)) == 11.
d. Write a function called continued_fraction(x, max_terms=10) that computes the continued fraction representation of a float x as a list of integers:
    x = a0 + 1/(a1 + 1/(a2 + ...))  
   Algorithm: a_i = floor(x); x = 1/(x - a_i); repeat. Stop when x is very close to an integer or max_terms is reached.
   Then reconstruct the rational approximation as a Fraction by folding the list from right to left.
   Test: continued_fraction(math.pi, 5) should give a good approximation of pi.
"""
print("\nEXTENSION 1")

# 1.a-b
class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0: raise ValueError("Denominator can't be zero.")

        gcd = math.gcd(abs(numerator), abs(denominator))
        num, den = numerator // gcd, denominator // gcd

        if den < 0: num, den = -num, -den

        self.numerator = num
        self.denominator = den

    def __str__(self):
        return f'{self.numerator}/{self.denominator}' if self.denominator != 1 else str(self.numerator)
    
    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'
    
    def __add__(self, other):
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)

        n_num: int = self.numerator * other.denominator + self.denominator * other.numerator
        n_den: int = self.denominator * other.denominator
        return Fraction(n_num, n_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)
        
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rsub__(self, other):
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)
        return other.__sub__(self)

    def __mul__(self, other):
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)
        
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)
        if other.numerator == 0: raise ZeroDivisionError("Cannot divide by zero.")
        
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __rtruediv__(self, other):
        if self.numerator == 0: raise ZeroDivisionError("Cannot divide by zero.")
        VALID_TYPES: tuple = (int, Fraction)
        if type(other) not in VALID_TYPES: return NotImplemented
        if type(other) == int: other = Fraction(other, 1)
        return other.__truediv__(self)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(-self.numerator, self.denominator) if self.numerator < 0 else self

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator) if type(other) == Fraction else NotImplemented

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator if type(other) == Fraction else NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __float__(self):
        return float(self.numerator) / float(self.denominator)

# 1.c
def farey_sequence(n: int) -> list:
    if n < 1: return []
    unique_fractions: list= []
    for q in range(1, n + 1):
        for p in range(0, q + 1):
            frac = Fraction(p, q)
            if frac not in unique_fractions:
                unique_fractions.append(frac)
    return sorted(unique_fractions)

# 1.d
def continued_fraction(x: float, max_terms: int = 10) -> tuple:
    coefficients: list = []
    current_x: float = x
    
    for i in range(max_terms):
        a = math.floor(current_x)
        coefficients.append(a)
        remainder: float = current_x - a
        if abs(remainder) < 1e-10: break
        current_x = 1.0 / remainder

    if not coefficients: return coefficients, Fraction(0, 1)
    result = Fraction(coefficients[-1], 1)
    
    for i in range(len(coefficients) - 2, -1, -1):
        result = Fraction(coefficients[i], 1) + Fraction(1, 1) / result
        
    return (coefficients, result)