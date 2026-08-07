## EXERCISES


# 1. Ask a virtual assistant
"""
a)
Because Python reserves that word to define a class in the code — if you used that same word for a variable or function name, there would be an error when the code is parsed. The same applies to every KEYWORD: they can't be used because they already have a predefined role.

b)
Because they are built-in functions, and if we decide to assign a value to one of them, we lose that function's functionality. For example, if we define:
- int = 123
Then if at some point we wanted to use the built-in function int; that is, convert some numeric-like data type to an integer, such as:
- int("12")
We won't be able to, because we assigned the value "123" to int and we can no longer use its properties.

c)
The most commonly used functions are:
- Type constructors
  int, float, complex, str, bool, bytes, bytearray, list, tuple, set, frozenset, dict
- Math
  abs, round, pow, divmod, max, min, sum
- Iteration & sequences
  len, range, enumerate, zip, map, filter, reversed, sorted, next, iter
- I/O
  print, input, open
- Object inspection
  type, isinstance, issubclass, id, dir, vars, hasattr, getattr, setattr, delattr, callable
- Conversion & representation
  bin, oct, hex, ord, chr, repr, format, hash
- Code execution
  eval, exec, compile, globals, locals
- Classes & objects
  object, super, property, classmethod, staticmethod, __import__
- Functional
  any, all, reduce (note: reduce is in functools, not built-in)
- Memory & misc
  memoryview, slice, help, breakpoint, NotImplemented, Ellipsis

d)
* Constants
  Variable                          Value
  - math.pi                         3.141592653589793
  - math.e                          2.718281828459045
  - math.tau                        6.283185307179586 (= 2π)
  - math.inf                        ∞
  - math.nan                        Not a Number

* Functions
  Rounding
  - ceil, floor, trunc
  Arithmetic
  - abs, factorial, gcd, lcm, pow, prod, remainder, fsum, isclose, isfinite, isinf, isnan
  Square root & exponential
  - sqrt, exp, exp2, expm1, log, log2, log10, log1p
  Trigonometric
  - sin, cos, tan, asin, acos, atan, atan2
  Hyperbolic
  - sinh, cosh, tanh, asinh, acosh, atanh
  Angle conversion
  - degrees, radians
  Special
  - gamma, lgamma, erf, erfc, comb, perm, hypot, dist, copysign

* Other modules
- os         : interact with the operating system (files, paths, environment variables)
- sys        : interact with the Python interpreter itself
- re         : regular expressions
- json       : read and write JSON
- datetime   : dates and times
- random     : random number generation
- math       : mathematical functions
- collections: advanced data structures (deque, Counter, defaultdict)
- itertools  : efficient iteration tools
- functools  : functional programming tools (reduce, lru_cache, partial)
- pathlib    : modern file path handling
- logging    : structured logging
- unittest   : testing
"""


# 2. Exercise
"""
a)
17 = n is illegal because, by the same analysis, it is analogous to KEYWORDS: while 17 itself is not one, it does have a predefined value that Python interprets as the numeric value 17 (possibly parsed as such internally).

b)
Both variables take the value 1 in: x = y = 1

c)
Apparently nothing — Python ignores it, as if it had never been written.

d)
A syntax error.

e)
An error because the module cannot be found, since it must be declared with its correct name, which in this case is "math".
"""


# 3. Exercise
import math
print("\nEXERCISE 3")

# part 1
radius = 5                                  # centimeters
volume = pow(radius, 3) * 4 * math.pi / 3   # cubic centimeters
print(volume)

# part 2
x = 42
result = pow(math.cos(x), 2) + pow(math.sin(x), 2)
print(result)

# part 3
print(math.e ** 2)      # correct
print(pow(math.e, 2))   # correct
print(math.exp(2))      # correct