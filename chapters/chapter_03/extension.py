## EXTENSIONS
import math

# 1. Extension - Numeric instability in sequence computation
"""
The following formula computes the n-th term of an arithmetic sequence:
- a_n = a_0 + n * d
where a_0 is the first term, d is the common difference, and n is the step index.

Tasks:
a. Set a_0 = 0.1, d = 0.1, and compute a_9 (the 10th term, n=9) using the formula. Store it in a variable called term_formula.
b. Now compute the same value by adding 0.1 nine times cumulatively: cumulative = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 (Yes, write it out explicitly. No loops yet).
c. Print both values. Are they equal? Use == to check and print the result.
d. Compute the absolute difference between the two. Is it exactly zero?
e. Comment explaining why these two computations may diverge. This is called floating-point accumulation error, and it is a real problem in numerical computing (your Álgebra Lineal will hit this eventually).
"""
print("\nEXTENSION 1")
a_0, d = 0.1, 0.1

# 1.a
a_9 = a_0 + d * 9
print("a_9: a_0 + n * d = " + str(a_9))

# 1.b
cumulative = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(cumulative)

# 1.c
print(cumulative == a_9)

# 1.d
print(abs(cumulative - a_9))

# 1.e
"""
This happens because decimals in Python are stored in bytes and cannot be represented exactly — there are limits. It's similar to 0.3333..., where even though 1/3 is a repeating decimal, a computer cannot express infinite decimals, so at some point it has to round in order to operate. That's why, during cumulative sums, the tiny rounding errors in each decimal keep accumulating and eventually become noticeable.
"""


# 2. Extension - Unit analysis and the math module
"""
Import math. You are given:
- angle_degrees = 45
- radius_cm = 10

Tasks:
a. Convert angle_degrees to radians. Don't use hardcode 3.14159. Store it in angle_radians.
b. Compute the x and y coordinates of a point on a circle.
c. Verify Pythagoras, print the result and the absolute difference from 100.
d. Now compute the same coordinates but introduce a DELIBERATE bug: pass angle_degrees (not angle_radians). Store in x_wrong, y_wrong. Compute x_wrong2 + y_wrong2 and print it. Comment: does Pythagoras still hold? What is the magnitude of the error?
e. This is a semantic error (chapter 2 vocabulary). Write a comment explaining why Python cannot catch this for you, and what defensive strategy you would use in a real pipeline to prevent it.
"""
print("\nEXTENSION 2")
angle_degrees = 45
radius_cm = 10

# 2.a
angle_radians = angle_degrees * math.pi / 180

# 2.b
x, y = radius_cm * math.cos(angle_radians), radius_cm * math.sin(angle_radians)
print("x: " + str(x) + ", y = " + str(y))

# 2.c
result = pow(x, 2) + pow(y, 2)
print(abs(100 - result))

# 2.d
x_wrong, y_wrong = radius_cm * math.cos(angle_degrees), radius_cm * math.sin(angle_degrees)
result_wrong = pow(x_wrong, 2) + pow(y_wrong, 2)
print(abs(100 - result_wrong))
"""
The result still holds despite the angle mistake because, even though it's not the angle we intended, the sides remain consistent relative to the originally chosen radius — that's why Pythagoras' theorem still checks out when we use it.
"""

# 2.e
"""
Because this isn't a syntax error or anything related to the language itself
— it's an interpretation error, like the following example:
- Imagine we want to perform the following operation: (3 + 6) / 3, expecting
  a result of 3; however, when writing the math operation we instead write:
    3 + 6 / 3   =>   4
  Even though there's no syntax error, there is an interpretation error, because we failed to express the intended math operation correctly, so we don't get the expected result.
"""


# 3. Extension - Significant figures and scientific notation
"""
Import math. In experimental data, measurements have limited precision. Reporting more digits than justified is scientifically wrong.

Tasks:
a. Compute math.e ** math.pi (e raised to pi). Store it in result. Print result with full precision.
b. Compute the same value rounded to 4 significant figures. Store the rounded value in result_4sf.
c. Compute the relative error between result and result_4sf.
d. What is the minimum number of significant figures needed so that the relative error is less than 1e-6?
"""
print("\nEXTENSION 3")

# 3.a
result = math.e ** math.pi
print(result)

# 3.b
result_4sf = round(result, 4 - 1 - math.floor(math.log10(result)))
print(result_4sf)

# 3.c
relative_error = abs(result_4sf - result) / abs(result)
print(relative_error)

# 3.d
result_4sf = round(result, 6 - 1 - math.floor(math.log10(result)))     # 6 sf
relative_error = abs(result_4sf - result) / abs(result)
print(relative_error < 1e-6)


# 4. Extension Variable naming as documentation
"""
Bad variable names are a maintenance hazard in data pipelines.
You are given this opaque but correct computation:
a = 6371
b = 3.141592653589793
c = 40.7128
d = -74.0060
e = 48.8566
f = 2.3522
g = (c - e)
h = (d - f)
i = (math.sin(math.radians(g) / 2)) ** 2
j = math.cos(math.radians(c)) * math.cos(math.radians(e))
k = (math.sin(math.radians(h) / 2)) ** 2
l = i + j * k
m = 2 * a * math.asin(math.sqrt(l))
print(m)

Tasks:
a. Run it and observe the output.
b. Figure out what this computes. (Hint: the numbers 6371, 40.7128/-74.0060, 48.8566/2.3522 are not random. Look them up.)
c. Rewrite the entire computation with proper variable names. Every variable must have a name that makes its purpose obvious without comments.
d. Add a docstring-style comment block at the top explaining what the computation does, what the inputs are, and what units the output is in.
e. Verify that your rewritten version produces the same numerical result.

This is the Haversine formula. You will encounter it or formulas like it
"""
print("\nEXTENSION 4")

# 4.a
a = 6371
b = 3.141592653589793
c = 40.7128
d = -74.0060
e = 48.8566
f = 2.3522
g = (c - e)
h = (d - f)
i = (math.sin(math.radians(g) / 2)) ** 2
j = math.cos(math.radians(c)) * math.cos(math.radians(e))
k = (math.sin(math.radians(h) / 2)) ** 2
l = i + j * k
m = 2 * a * math.asin(math.sqrt(l))
print(m)

# 4.b
"""
This code computes the distance between New York City and Paris using the Haversine formula. The numbers correspond to the Earth's radius and each city's coordinates.
"""

# 4.c
earth_radius_km = 6371              # km
lat_new_york = 40.7128
lon_new_york = -74.0060
lat_paris = 48.8566
lon_paris = 2.3522
lat_diff = lat_new_york - lat_paris
lon_diff = lon_new_york - lon_paris
lat_term = (math.sin(math.radians(lat_diff) / 2)) ** 2
lat_factor = math.cos(math.radians(lat_new_york)) * math.cos(math.radians(lat_paris))
lon_term = (math.sin(math.radians(lon_diff) / 2)) ** 2
haversine_value = lat_term + lat_factor * lon_term
distance_km = 2 * earth_radius_km * math.asin(math.sqrt(haversine_value))
print("The distance between New York and Paris is: " + str(distance_km) + " km")

# 4.d
"""
This code computes the great-circle (straight-line, over the surface) distance between two given locations (New York and Paris) using the Haversine formula. The code assumes the Earth is a perfect sphere.
Coordinates:
  - lat_new_york: 40.7128° N
  - lon_new_york: -74.0060° W
  - lat_paris: 48.8566° N
  - lon_paris: 2.3522° E
Constants:
  - earth_radius_km: 6371 km
Output:
  - distance_km
"""