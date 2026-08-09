## EXTENSIONS
import math


# 1. Extension 1 - Recursive return values and mathematical induction
"""
Tasks:
a. Write a recursive function called power(base, exp) that computes base**exp WITHOUT using ** or math.pow. Add input validation: exp must be a non-negative integer.
b. Write a recursive function called fast_power(base, exp) that uses FAST EXPONENTIATION (also called exponentiation by squaring):
- if exp == 0: return 1
if exp % 2 == 0: half = fast_power(base, exp // 2); return half * half
else: return base * fast_power(base, exp - 1)
This reduces the number of recursive calls from O(n) to O(log n). Test: fast_power(2, 10) == 1024, fast_power(3, 7) == 2187. Count the recursive calls in each version for exp=16:
- power(2, 16): how many calls?
fast_power(2, 16): how many calls?
Add a counter using a print statement in each to verify.
c. Write a recursive function called binomial_coefficient(n, k) that computes C(n, k) = n! / (k! * (n-k)!) using Pascal's triangle recurrence:
- C(n, 0) = 1
C(n, n) = 1
C(n, k) = C(n-1, k-1) + C(n-1, k)
Add input validation: n and k must be non-negative integers, k <= n.
- Test: C(5,2)=10, C(10,3)=120, C(20,10)=184756.
"""
print("\nEXTENSION 1")

# 1.a
def power(base: float, exp: int) -> float:
    """
    Recursively compute base ** exp without using ** or math.pow.

    Parameters
    ----------
    base : float
        The base value.
    exp : int
        Non-negative integer exponent.

    Returns
    -------
    float
        base raised to the power exp, or -1 if exp is negative (error case).
    """
    if exp < 0: return -1  # Error case: -1
    # print("count")
    if exp == 1: return base
    return base * power(base, exp - 1)

# 1.b
def fast_power(base: float, exp: int) -> float:
    """
    Recursively compute base ** exp using exponentiation by squaring, reducing the call count from O(n) to O(log n).

    Parameters
    ----------
    base : float
        The base value.
    exp : int
        Non-negative integer exponent.

    Returns
    -------
    float
        base raised to the power exp, or -1 if exp is negative (error case).
    """
    if exp < 0: return -1  # Error case: -1
    # print("count")
    if exp == 0: return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2)
        return half * half
    else: return base * fast_power(base, exp - 1)
print(fast_power(2, 10) == 1024)
print(fast_power(3, 7) == 2187)
power(2, 16)        # 16 recursive calls
fast_power(2, 16)   # 6 recursive calls

# 1.c
def binomial_coefficient(n: int, k: int) -> int:
    """
    Recursively compute the binomial coefficient C(n, k) using Pascal's triangle recurrence.

    Parameters
    ----------
    n : int
        Non-negative integer.
    k : int
        Non-negative integer. Must be <= n.

    Returns
    -------
    int
        C(n, k) = n! / (k! * (n - k)!).
    """
    if k == 0: return 1
    if n == k: return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
print(binomial_coefficient(5, 2) == 10)
print(binomial_coefficient(10, 3) == 120)
print(binomial_coefficient(20, 10) == 184756)


# 2. Extension 2 - Pure functions and function composition
"""
Tasks:
a. Write pure functions for the following transformations (no print, no side effects):
- normalize(x, min_val, max_val) -> maps x to [0, 1]; formula: (x - min_val) / (max_val - min_val)
- denormalize(x_norm, min_val, max_val) -> inverse of normalize
- clamp(x, low, high) -> returns low if x < low, high if x > high, else x
- sigmoid(x) -> 1 / (1 + math.e ** (-x)); This is the activation function used in logistic regression and neural networks.
- relu(x) -> max(x, 0) without using max() (write it with a conditional expression or if/else)
b. Test the round-trip property: for any x in [min_val, max_val], denormalize(normalize(x, a, b), a, b) == x (up to float precision). Test with (x=37, min=35, max=42) and verify the absolute difference < 1e-10.
c. Write a function called apply_pipeline(x, min_val, max_val) that:
- normalizes x to [0,1]
- applies sigmoid to the normalized value
- clamps the result to [0.05, 0.95] (remove extreme predictions); This is a toy version of what a logistic regression output layer does. Return the result. No print, no side effects.
d. Write a function called batch_pipeline(x1, x2, x3, min_val, max_val) that applies apply_pipeline to each of three values and returns all three. (Again, no lists yet — three separate parameters.) Verify that the output values are all in [0.05, 0.95].
"""
print("\nEXTENSION 2")

# 2.a
def normalize(x: float, min_val: float, max_val: float) -> float:
    """
    Map a value from [min_val, max_val] to [0, 1].

    Parameters
    ----------
    x : float
        The value to normalize.
    min_val : float
        Lower bound of the original range.
    max_val : float
        Upper bound of the original range.

    Returns
    -------
    float
        The normalized value.
    """
    return (x - min_val) / (max_val - min_val)

def denormalize(x_norm: float, min_val: float, max_val: float) -> float:
    """
    Map a normalized value in [0, 1] back to [min_val, max_val].

    Parameters
    ----------
    x_norm : float
        The normalized value, in [0, 1].
    min_val : float
        Lower bound of the target range.
    max_val : float
        Upper bound of the target range.

    Returns
    -------
    float
        The denormalized value.
    """
    return x_norm * (max_val - min_val) + min_val

def clamp(x: float, low: float, high: float) -> float:
    """
    Restrict a value to a given range.

    Parameters
    ----------
    x : float
        The value to clamp.
    low : float
        Lower bound.
    high : float
        Upper bound.

    Returns
    -------
    float
        low if x < low, high if x > high, otherwise x.
    """
    if x < low: return low
    if x > high: return high
    return x

def sigmoid(x: float) -> float:
    """
    Compute the logistic sigmoid function.

    Parameters
    ----------
    x : float
        Input value.

    Returns
    -------
    float
        1 / (1 + e**(-x)), in the range (0, 1).
    """
    return 1 / (1 + math.e ** (-x))

def relu(x: float) -> float:
    """
    Compute the ReLU (rectified linear unit) activation, without using the built-in max().

    Parameters
    ----------
    x : float
        Input value.

    Returns
    -------
    float
        x if x > 0, otherwise 0.
    """
    return x if x > 0 else 0

# 2.b
print(abs(denormalize(normalize(37, 35, 42), 35, 42) - 37) < 1e-10)

# 2.c
def apply_pipeline(x: float, min_val: float, max_val: float) -> float:
    """
    Normalize a value, apply the sigmoid function, and clamp the result to a safe prediction range.

    Parameters
    ----------
    x : float
        The raw input value.
    min_val : float
        Lower bound used for normalization.
    max_val : float
        Upper bound used for normalization.

    Returns
    -------
    float
        The final value, clamped to [0.05, 0.95].
    """
    x = normalize(x, min_val, max_val)
    x = sigmoid(x)
    return clamp(x, 0.05, 0.95)

# 2.d
def batch_pipeline(x1: float, x2: float, x3: float, min_val: float, max_val: float) -> tuple[float, float, float]:
    """
    Apply apply_pipeline to three values and return all three results.

    Parameters
    ----------
    x1 : float
        First raw input value.
    x2 : float
        Second raw input value.
    x3 : float
        Third raw input value.
    min_val : float
        Lower bound used for normalization.
    max_val : float
        Upper bound used for normalization.

    Returns
    -------
    tuple[float, float, float]
        The pipeline output for x1, x2, and x3, in that order.
    """
    return apply_pipeline(x1, min_val, max_val), apply_pipeline(x2, min_val, max_val), apply_pipeline(x3, min_val, max_val)
print(batch_pipeline(36, 37, 38, 35, 42))


# 3. Extension 3 - Incremental development with a non-trivial target
"""
Tasks:
Apply the incremental development process from section 6.4 to a function that is complex enough to require it.

Target: write a function called quadratic_roots(a, b, c) that returns both roots of ax^2 + bx + c = 0 using the quadratic formula:
    x = (-b ± sqrt(b^2 - 4ac)) / (2a)

Do NOT just write the final version. Follow these steps explicitly:

Step 1: Write a version that always returns (0.0, 0.0).
Step 2: Add the discriminant computation. Print and verify for (1, -3, 2) -> discriminant = 1.
Step 3: Add the square root. Print and verify.
Step 4: Add both roots. Print and verify: roots of x^2-3x+2=0 are (2.0, 1.0).
Step 5: Add input validation:
   - a == 0: not a quadratic, return None and print error
   - discriminant < 0: complex roots, return None and print "Complex roots: no real solution"
   - discriminant == 0: double root, return (root, root)
Step 6: Remove all print statements (scaffolding). Final function returns only values.

Test cases (verify all):
   quadratic_roots(1, -3, 2)   -> (2.0, 1.0)
   quadratic_roots(1, 2, 1)    -> (-1.0, -1.0)  [double root]
   quadratic_roots(1, 0, 1)    -> None          [complex roots]
   quadratic_roots(0, 2, 1)    -> None          [not quadratic]
   quadratic_roots(2, -4, 2)   -> (1.0, 1.0)
"""
print("\nEXTENSION 3")

# --- Step 1: always returns (0.0, 0.0) ---
def quadratic_roots(a, b, c):
    return 0.0, 0.0
print("Step 1:", quadratic_roots(1, -3, 2))   # scaffolding, expected (0.0, 0.0)

# --- Step 2: add discriminant computation ---
def quadratic_roots(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    print("Step 2 - discriminant:", discriminant)
    return 0.0, 0.0
quadratic_roots(1, -3, 2)   # verify: discriminant should print as 1

# --- Step 3: add the square root ---
def quadratic_roots(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    w = math.sqrt(discriminant)
    print("Step 3 - sqrt(discriminant):", w)
    return 0.0, 0.0
quadratic_roots(1, -3, 2)   # verify: sqrt(1) should print as 1.0

# --- Step 4: add both roots (not yet dividing by 'a', only by 2 - known
#             incomplete on purpose, fixed in step 5) ---
def quadratic_roots(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    w = math.sqrt(discriminant)
    roots = (- b + w) / 2, (- b - w) / 2
    print("Step 4 - roots (not yet divided by a):", roots)
    return roots
quadratic_roots(1, -3, 2)   # verify: for a=1 this coincidentally matches (2.0, 1.0)

# --- Step 5: add input validation and the missing division by 'a' ---
def quadratic_roots(a, b, c):
    if a == 0:
        print("Error: a == 0, this is not a quadratic equation.")
        return None
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant < 0:
        print("Complex roots: no real solution")
        return None
    if discriminant == 0:
        return (-b) / (2*a), (-b) / (2*a)
    w = math.sqrt(discriminant)
    return (- b + w) / (2*a), (- b - w) / (2*a)
print("Step 5:", quadratic_roots(1, -3, 2))
print("Step 5:", quadratic_roots(2, -4, 2))    # this is where step 4's missing '/a' would have failed

# --- Step 6: final version, scaffolding prints removed ---
def quadratic_roots(a, b, c):
    """
    Compute both real roots of the quadratic equation ax^2 + bx + c = 0.

    Parameters
    ----------
    a : float
        Quadratic coefficient. Must not be zero.
    b : float
        Linear coefficient.
    c : float
        Constant term.

    Returns
    -------
    tuple[float, float] or None
        Both roots (equal, in the case of a double root), or None if 'a' is zero or the discriminant is negative (complex roots).
    """
    if a == 0:
        return None
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant < 0:
        return None
    if discriminant == 0:
        return (-b) / (2*a), (-b) / (2*a)
    w = math.sqrt(discriminant)
    return (- b + w) / (2*a), (- b - w) / (2*a)

print(quadratic_roots(1, -3, 2))   # -> (2.0, 1.0)
print(quadratic_roots(1, 2, 1))    # -> (-1.0, -1.0)  [double root]
print(quadratic_roots(1, 0, 1))    # -> None          [complex roots]
print(quadratic_roots(0, 2, 1))    # -> None          [not quadratic]
print(quadratic_roots(2, -4, 2))   # -> (1.0, 1.0)
