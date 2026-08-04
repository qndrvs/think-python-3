## EXERCISES

# 1. Ask a virtual assistant
"""
a)
We can interpret these operations as boolean algebra with base-2 numbers, comparing the numbers at each respective place value. For example:
- 7: 111 (base 2)
- 2: 010 (base 2)
Here we can interpret "1" as TRUE, and "0" as FALSE. The first-order digit for 7 and 2 is, respectively, 1 and 0; for the second order, 1 and 1; for the third order, 1 and 0.
If we want to operate 7 XOR 2, we operate on each place value independently:
- First order:  1 XOR 0 => 1
- Second order: 1 XOR 1 => 0
- Third order:  1 XOR 0 => 1
XOR can be interpreted as the negation of the biconditional. The resulting number of 7 XOR 2 is: 101; converting this from base 2 to decimal gives us: 5
Therefore, we affirm that: 7 XOR 2 => 5

b)
1. ()          — Parentheses
2. **          — Exponentiation
3. +x, -x, ~x  — Unary operators
4. *, /, //, % — Multiplication, division, floor division, modulo

c)
The round() function takes two arguments:
- round(number, n_digits)
Where the second argument represents the number of decimal places the number will be rounded to. It's important to mention that it rounds to the nearest EVEN NUMBER (banker's rounding).

d)
The "%" operator gives us the remainder of integer division between two numbers, which don't necessarily have to be integers.
"""


# 2. Exercise
"""
The round() function, as mentioned before, rounds the number to the nearest even number.
"""


# 3. Exercise
"""
1. The standard sign rules apply.

2. A syntax error occurs, and Python suggests adding a comma between them.

3. A syntax error occurs again.
"""


# 4. Exercise
print("\nEXERCISE 4")
print(type(765))         # int
print(type(2.718))       # float
print(type('2 pi'))      # str
print(type(abs(-7)))     # int
print(type(abs(-7.0)))   # float
print(type(abs))         # function -> builtin_function_or_method
print(type(int))         # type
print(type(type))        # type


# 5. Exercise
print("\nEXERCISE 5")
print(42 * 60 + 42)                        # a)
print(10 / 1.61)                           # b)
print((10 / 1.61) / (42 * 60 + 42))        # c)
print((10 / 1.61) / (42 * 60 + 42))        # d.1) seconds
print((10 / 1.61) / (42 * 60 + 42) * 60)   # d.2) minutes
print((10 / 1.61) / (42 * 60 + 42) * 3600) # d.3) hours