## EXTENSIONS


# 1. Extension 1 - Boolean logic and De Morgan's laws
"""
Tasks:
a. You receive a sensor reading: value = 87.3
   Write a single boolean expression (no if statement) that is True if and only if:
   - value is between 0 and 100 inclusive
   - value is not equal to exactly 50.0
   - value is not a multiple of 10
b. Write the SAME logical condition using De Morgan's law:
   - not (A or B or C) == (not A) and (not B) and (not C)
   Apply it to negate your condition from step 1 and simplify.
c. Write a function called is_valid_reading(value, low, high, excluded) that returns True if:
   - value is within [low, high]
   - value is not exactly equal to excluded
   Use a single return statement with a boolean expression — no if/else.
d. Write a function called is_outlier(value, mean, std_dev, threshold=3)
   that returns True if the absolute z-score exceeds threshold:
       |value - mean| / std_dev > threshold
   This is the standard 3-sigma outlier detection rule.
   Add input validation: if std_dev <= 0, return None and print an error.
"""
print("\nEXTENSION 1")
value = 87.3

# 1.a
print((0 <= value <= 100) and (value != 50.0) and (value % 10 != 0))

# 1.b
print(not ((0 > value and value > 100) or (value == 50.0) or (value % 10 == 0)))

# 1.c
def is_valid_reading(value: float, low: float, high: float, excluded: float) -> bool:
   """
   Check whether a reading falls within a range and is not an excluded value.

   Parameters
   ----------
   value : float
       The reading to validate.
   low : float
       Lower bound of the valid range (inclusive).
   high : float
       Upper bound of the valid range (inclusive).
   excluded : float
       A specific value that is considered invalid even if in range.

   Returns
   -------
   bool
       True if 'value' is within [low, high] and is not exactly 'excluded'; False otherwise.
   """
   return (low <= value <= high) and value != excluded

# 1.d
def is_outlier(value: float, mean: float, std_dev: float, threshold: float = 3.0) -> bool:
   """
   Determine whether a value is a statistical outlier using the 3-sigma rule.

   Parameters
   ----------
   value : float
       The value to check.
   mean : float
       Mean of the reference distribution.
   std_dev : float
       Standard deviation of the reference distribution. Must be > 0.
   threshold : float, optional
       Number of standard deviations beyond which a value is considered an outlier (default is 3.0).

   Returns
   -------
   bool
       True if the absolute z-score of 'value' exceeds 'threshold'.

   Raises
   ------
   ValueError
       If 'std_dev' is less than or equal to 0.
   """
   if std_dev <= 0: raise ValueError("Standard deviation cannot be zero or negative.")
   return abs(value - mean) / std_dev > threshold


# 2. Extension 2 - Recursion and the call stack as a data structure
"""
Tasks:
a. Write a recursive function called digit_sum(n) that returns the sum of the digits of a positive integer n.
   Example: digit_sum(12345) == 15
b. Write a recursive function called digital_root(n) that repeatedly applies digit_sum until the result is a single digit.
   Example: digital_root(9875) -> digit_sum(9875) = 29 -> digit_sum(29) = 11 -> digit_sum(11) = 2 -> return 2
   Mathematical property: digital_root(n) == 1 + (n-1) % 9 for n > 0. Verify your function matches this formula for n = 1 through 20.
c. Write a recursive function called count_digits(n) that returns the number of digits in a positive integer. Do NOT convert to string. Use // 10 to reduce.
   Verify: count_digits(10**k) == k+1 for k = 0, 1, 2, 3, 4, 5.
d. Write a recursive function called is_palindrome_number(n) that returns True if the integer reads the same forwards and backwards.
   Example: is_palindrome_number(12321) -> True
            is_palindrome_number(12345) -> False
"""
print("\nEXTENSION 2")

# 2.a
def digit_sum(n: int) -> int:
   """
   Recursively compute the sum of the digits of a positive integer.

   Parameters
   ----------
   n : int
       A positive integer.

   Returns
   -------
   int
       The sum of the digits of n.
   """
   if n < 10: return n
   return n % 10 + digit_sum(n // 10)
print(digit_sum(12345))

# 2.b
def digital_root(n: int) -> int:
   """
   Recursively reduce a positive integer to its digital root (repeated digit-sum until a single digit remains).

   Parameters
   ----------
   n : int
       A positive integer.

   Returns
   -------
   int
       The digital root of n (a single digit, 0-9).
   """
   if n < 10: return n
   return digital_root(digit_sum(n))
m = 0
for i in range(1, 21):
   if digital_root(i) == 1 + (i-1) % 9: m += 1
print(m == 20)

# 2.c
def count_digits(n: int) -> int:
   """
   Recursively count the number of digits in a positive integer, without converting it to a string.

   Parameters
   ----------
   n : int
       A positive integer.

   Returns
   -------
   int
       The number of digits in n.
   """
   if n < 10: return 1
   return 1 + count_digits(n // 10)
m = 0
for i in range(6):
   if count_digits(10**i) == i+1: m += 1
print(m == 6)

# 2.d
def is_palindrome_number(n: int) -> bool:
   """
   Recursively check whether an integer reads the same forwards and backwards.

   Parameters
   ----------
   n : int
       A positive integer.

   Returns
   -------
   bool
       True if n is a numeric palindrome, False otherwise.
   """
   if n < 10: return True
   return ((n // (10 ** (count_digits(n) - 1))) == n % 10) and is_palindrome_number((n % (10 ** (count_digits(n) - 1))) // 10)
print(is_palindrome_number(12321))
print(is_palindrome_number(12345))


# 3. Extension 3 - Chained conditionals as a classifier
"""
Tasks:
a. Write a function called classify_bmi(weight_kg, height_m) that:
   - Computes BMI = weight_kg / height_m**2
   - Returns the WHO classification string:
       BMI < 18.5       -> 'Underweight'
       18.5 <= BMI < 25 -> 'Normal weight'
       25 <= BMI < 30   -> 'Overweight'
       BMI >= 30        -> 'Obese'
   Add input validation: weight and height must be positive floats.
b. Write a function called classify_temperature_anomaly(temp, baseline, std) that classifies a temperature reading relative to a baseline:
       temp < baseline - 2*std    -> 'Cold anomaly'
       baseline - 2*std <= temp <= baseline + 2*std  -> 'Normal'
       temp > baseline + 2*std    -> 'Warm anomaly'
   This is a simplified anomaly detection pattern used in climate data.
c. Write a function called fizzbuzz_extended(n) that returns:
   - 'FizzBuzzBang' if divisible by 3, 5, AND 7
   - 'FizzBuzz' if divisible by 3 AND 5 (but not 7)
   - 'FizzBang' if divisible by 3 AND 7 (but not 5)
   - 'BuzzBang' if divisible by 5 AND 7 (but not 3)
   - 'Fizz' if divisible by 3 only
   - 'Buzz' if divisible by 5 only
   - 'Bang' if divisible by 7 only
   - str(n) otherwise
   ORDER MATTERS. Write a comment explaining why the order of the conditions is critical and what bug arises if you check 'Fizz' before 'FizzBuzz'.
d. Write a recursive function called collatz(n) that:
   - If n == 1, returns 1
   - If n is even, recurses with n // 2
   - If n is odd, recurses with 3*n + 1
   Returns the NUMBER OF STEPS to reach 1, not the sequence.
   The Collatz conjecture states this always terminates — no one has proved it.
   Test: collatz(27) should return 111.
"""
print("\nEXTENSION 3")

# 3.a
def classify_bmi(weight_kg: float, height_m: float) -> str:
   """
   Classify a person's BMI according to the WHO categories.

   Parameters
   ----------
   weight_kg : float
       Body weight in kilograms. Must be positive.
   height_m : float
       Height in meters. Must be positive.

   Returns
   -------
   str
       One of 'Underweight', 'Normal weight', 'Overweight', 'Obese'.

   Raises
   ------
   ValueError
       If 'weight_kg' or 'height_m' is not a positive value.
   """
   if weight_kg <= 0: raise ValueError("Weight must be a positive value (in kg).")
   if height_m <= 0: raise ValueError("Height must be a positive value (in m).")

   bmi = weight_kg / (height_m ** 2)

   if bmi < 18.5: return 'Underweight' 
   if 18.5 <= bmi < 25: return 'Normal weight'
   if 25 <= bmi < 30: return 'Overweight'
   if 30 <= bmi: return 'Obese'

# 3.b
def classify_temperature_anomaly(temp: float, baseline: float, std: float) -> str:
   """
   Classify a temperature reading relative to a baseline using a 2-sigma threshold.

   Parameters
   ----------
   temp : float
       The temperature reading to classify.
   baseline : float
       The reference (expected) temperature.
   std : float
       Standard deviation used to define the normal range.

   Returns
   -------
   str
       One of 'Cold anomaly', 'Normal', 'Warm anomaly'.
   """
   if temp < baseline - 2 * std: return 'Cold anomaly'
   if baseline - 2 * std <= temp <= baseline + 2 * std: return 'Normal'
   if temp > baseline + 2 * std: return 'Warm anomaly'

# 3.c
def fizzbuzz_extended(n: int) -> str:
   """
   Classify an integer according to its divisibility by 3, 5, and 7, combining labels when more than one applies.

   Parameters
   ----------
   n : int
       The integer to classify.

   Returns
   -------
   str
       A combination of 'Fizz' (div. by 3), 'Buzz' (div. by 5), and 'Bang' (div. by 7), concatenated in that fixed order for whichever divisors apply (e.g. 'FizzBuzzBang', 'FizzBang'), or str(n) if none apply.
   """
   result = ''
   if (n % 3 == 0):
      result += 'Fizz'
   if (n % 5 == 0):
      result += 'Buzz'
   if (n % 7 == 0):
      result += 'Bang'
   if result == '':
      result = str(n)
   return result

# 3.d
def collatz(n: int, steps: int = 0) -> int:
   """
   Recursively compute the number of steps needed for the Collatz sequence starting at n to reach 1.

   Parameters
   ----------
   n : int
       Starting positive integer.
   steps : int, optional
       Accumulator used internally to count steps (default is 0).

   Returns
   -------
   int
       The number of steps required to reach 1.
   """
   if n == 1:
      return steps
   if n % 2 == 0:
      return collatz(n // 2, steps + 1)
   else:
      return collatz(3 * n + 1, steps + 1)
print(collatz(27))      # 111
