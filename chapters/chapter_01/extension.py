## EXTENSION

# 1. Extension - Floating-point precision trap
"""
Python uses IEEE 754 double-precision floating point.
This means that some decimal numbers cannot be represented exactly in binary, and arithmetic on them produces surprising results.
Run this:
- 0.1 + 0.2 == 0.3
You will get False.

Tasks:
a. Without using any import or variable, write a single expression using round() that makes the comparison above return True. You are not allowed to hardcode 0.3, you must use 0.1 + 0.2 in the expression.
b. Explain in a comment WHY 0.1 + 0.2 is not exactly 0.3 in Python.
c. Write an expression using abs() and no variables that evaluates to True if the absolute difference between (0.1 + 0.2) and 0.3 is less than 1e-9. This is the standard way to compare floats in scientific computing (Hint: 1e-9 is valid Python notation, look up what it means if you don't know).
"""
print("\nEXTENSION 1")

# 1.a
0.1 + 0.2                           # 0.30000000000000004 = 0.3 + 4e-17 != 0.3
print(round(0.1 + 0.2, 2) == 0.3)   # 0.30 == 0.3  =>  True

# 1.b
print("Because decimals are not represented exactly in binary, we can see that when adding '0.1 + 0.2' we get a value of '0.3 + 4e-17'; that is why the inequality with '0.3' occurs.")

# 1.c
print(abs((0.1 + 0.2) - 0.3) < 1e-9)   # 1e-9 = 1 * pow(10, -9)


# 2. Extension - Type coercion cascade
"""
You are given the following nested expression. Do NOT run it yet.
- type(round(abs(int(float(int('0b1010', 2))))))

Tasks:
a. Trace the evaluation manually, step by step, from innermost to outermost. Write each intermediate result and its type as a comment. '0b1010' is a string — but int() accepts an optional base argument. What base does binary use? What is the decimal value of 0b1010?
b. Predict the final type and value before running it.
c. Now run it and verify. If you were wrong, explain why.
d. Without using variables, write your own nested expression of at least 5 function calls (using only round, abs, int, float, str, len, type) where the final result is the integer 42. Show that it returns 42 and that type() confirms it is int.
"""
print("\nEXTENSION 2")

# 2.a
int('0b1010', 2)   # 10     -     0b: prefix indicating the following number is expressed in base n; 1010: number expressed in base n; 2: base n => 10
float(10)          # 10.0
int(10.0)          # 10
abs(10)            # 10
round(10)          # 10
type(10)           # int
print("Binary uses base 2, so the decimal value of: 0b1010 = 1 * pow(2, 3) + 0 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0) = 8 + 0 + 2 + 0 = 10")

# 2.b
print("int")

# 2.c
print(type(round(abs(int(float(int('0b1010', 2)))))))   # I was right, I guessed "int" as the final result's type; and the printed message confirms: "<class 'int'>."

# 2.d
int(round(int(float(int('0b101010', 2)))))          # Expression
print(int(round(int(float(int('0b101010', 2))))))
print(type(int(round(int(float(int('0b101010', 2)))))))


# 3. Extension - Modulus as a data instrument
"""
Given a dataset recording timestamp in seconds from midnight: 90061; complete tasks without using variables and only using //, %, and arithmetic operators.

Tasks:
a. Compute how many complete days are in 90061 seconds.
b. Compute the remaining hours after removing full days.
c. Compute the remaining minutes after removing full hours.
d. Compute the remaining seconds after removing full minutes.
e. Now: given that a sensor fires every 7 seconds starting from second 0, and the current timestamp is 90061 seconds, compute how many seconds until the NEXT sensor firing.
"""
print("\nEXTENSION 3")

# 3.a
print("days:    " + str(90061 // (24 * 3600)))

# 3.b
print("hours:   " + str((90061 % (24 * 3600)) // 3600))

# 3.c
print("minutes: " + str((90061 % 3600) // 60))

# 3.d
print("seconds: " + str((90061 % 3600) % 60))

# 3.e
print("next sensor firing in " + str((7 - (90061 % 7)) % 7) + " seconds")


# 4. Extension - String as structured data
"""
You have the following raw string (treat it as a literal in your code):
- '  3.14159  '
Use only len(), int(), float(), str(), abs(), round(), +, *, the comparison operators, and string repetition/concatenation.

Tasks:
a. Compute the length of the string including whitespace.
b. Compute the length of the string WITHOUT whitespace. You cannot use .strip().
c. Compute the absolute difference between that float and 3.141592653589793.
d. Round the result to 5 decimal places and verify its type is float.
e. You receive a sensor ID as the string '00847'. Convert it to an integer, multiply by 3, convert back to string, and compute the length of the resulting string. All in one expression, no variables.
"""
print("\nEXTENSION 4")
raw_value = '  3.14159  '
sensor_id = '00847'

# 4.a
print(len(raw_value))

# 4.b
print(len(str(float(raw_value))))

# 4.c
print(abs(3.141592653589793 - float(raw_value)))

# 4.d
print(round(abs(3.141592653589793 - float(raw_value)), 5))
print(type(round(abs(3.141592653589793 - float(raw_value)), 5)))

# 4.e
print(len(str(int(id) * 3)))