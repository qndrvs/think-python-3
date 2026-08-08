## EXTENSIONS
import math


# 1. Extesion 1 - Interface design for a data formatter
"""
Tasks:
a. Write a function called format_row(label, value, width = 20) that prints:
   - label..........value
   Preconditions (document them in the docstring):
   - label must be a string
   - value can be int or float
   - width must be greater than len(label) + len(str(value)) + 1
b. Write a function called format_section(title, width=20) that prints:
   === TITLE ===
   centered, padded to the given width with '=== ' and ' ===' characters.
c. Write a function called format_report(title, labels, values, width=20) that:
   - prints a section header using format_section
   - prints one row per label/value pair using format_row
   BUT: you don't have lists yet. Instead, take exactly 3 labels and 3 values as separate parameters: label1, value1, label2, value2, label3, value3. This is ugly - and that's the point. Comment why this interface is bad and what you would change once you learn lists.
"""
print("\nEXTENSION 1")

# 1.a
def format_row(label: str, value: float, width: int = 20) -> None:
    """
    Format and print a single "label.....value" row.

    Parameters
    ----------
    label : str
        Label for the numeric value.
    value : float | int
        Numeric value associated with the label.
    width : int, optional
        Total width of the printed line (default is 20). Must be large enough to fit label, value, and at least one separating dot.

    Returns
    -------
    None
        The function only prints the formatted line; it returns nothing.

    Raises
    ------
    ValueError
        If 'width' does not allow at least one dot between 'label' and 'value'.
    TypeError
        If 'label' is not a string, 'value' is not numeric, or 'width' is not an integer.
    """
    if (type(label) != str) or (type(value) not in [float, int]) or (type(width) != int):
        raise TypeError("Invalid input type.")
    if width < len(label) + len(str(value)) + 1:
        raise ValueError(f"width must allow at least one dot between {label} and {value}.")

    print(label + "." * (width - len(label) - len(str(value))) + str(value))

# 1.b
def format_section(title: str, width: int = 20) -> None:
    """
    Print a centered section header framed with '=== ' and ' ==='.

    Parameters
    ----------
    title : str
        Title to display inside the header.
    width : int, optional
        Total width used to center the header (default is 20).

    Returns
    -------
    None
    """
    padding_per_side = math.ceil((width - len(title) - 8) / 2)
    print(" " * padding_per_side + f"=== {title} ===")

# 1.c
def format_report(title: str, label1: str, label2: str, label3: str, value1: str, value2: str, value3: int, width: int = 20) -> None:
    """
    Print a small report: a section header followed by three label/value rows.

    Parameters
    ----------
    title : str
        Report title, passed to format_section.
    label1, label2, label3 : str
        Labels for each of the three rows.
    value1, value2, value3 : int | float
        Values for each of the three rows.
    width : int, optional
        Total width used for both the header and each row (default is 20).

    Returns
    -------
    None
    """
    format_section(title, width)
    format_row(label1, value1, width)
    format_row(label2, value2, width)
    format_row(label3, value3, width)
"""
This interface is bad because, besides making it very easy to mix up labels and values, it forces an excessive number of parameters. Once I have lists, I could make a single parameter a list of labels, for example, and then iterate based on that list instead of hardcoding three of each.
"""
format_report("TESTING", "Temperature", "Altitude", "Time", 28, 100, 6, 30)


# 2. Extension - Refactoring a numeric pipeline
"""
You are given this working but poorly structured code:
-   import math

    # Pipeline: computes normalized score for 3 students
    raw1 = 47
    mean = (47 + 63 + 55) / 3
    std = math.sqrt(((47-mean)**2 + (63-mean)**2 + (55-mean)**2) / 3)
    z1 = (raw1 - mean) / std

    raw2 = 63
    mean = (47 + 63 + 55) / 3
    std = math.sqrt(((47-mean)**2 + (63-mean)**2 + (55-mean)**2) / 3)
    z2 = (raw2 - mean) / std

    raw3 = 55
    mean = (47 + 63 + 55) / 3
    std = math.sqrt(((47-mean)**2 + (63-mean)**2 + (55-mean)**2) / 3)
    z3 = (raw3 - mean) / std

    print(z1, z2, z3)

Tasks:
a. Apply the encapsulation and generalization pattern from chapter 4:
   - First, encapsulate the z-score computation into a function.
   - Then generalize so that mean and std are parameters (not recomputed inside).
   - Then write a helper function that computes the population std from 3 values.
b. Rewrite the pipeline using your functions. It should compute the same z-scores but with no repeated code.
"""
print("\nEXTENSION 2")

# 2.a
def calc(r1: float, r2: float, r3: float) -> None:
    """
    Compute and print the z-scores of three raw values relative to their own mean and population standard deviation.

    Parameters
    ----------
    r1 : float
        First raw value.
    r2 : float
        Second raw value.
    r3 : float
        Third raw value.

    Returns
    -------
    None
    """
    mean = (r1 + r2 + r3) / 3
    std = math.sqrt((pow(r1 - mean, 2) + pow(r2 - mean, 2) + pow(r3 - mean, 2)) / 3)
    z1, z2, z3 = (r1 - mean) / std, (r2 - mean) / std, (r3 - mean) / std
    print(z1, z2, z3)

# 2.b
calc(47, 63, 55)


# 3. Extension - Generalization and the parameter space
"""
Tasks:
a. Write a function called power_of_2_table(n) that prints a table of powers of 2 from 2^0 to 2^n:
       2^0 = 1
       2^1 = 2
       ...
       2^n = ...
b. Generalize it to power_table(base, n) for any base.
c. Generalize it further to power_table(base, start, end, step) where you print base^start, base^(start+step), base^(start+2*step), ... up to base^end.
d. Now you have OVER-generalized. Write a comment explaining:
   i)   What is the minimum parameter set that covers 95% of real use cases?
   ii)  Which parameters should have defaults and what should those defaults be?
   iii) What is the cost of over-generalization to the caller?
e. Write the "right" version of the function with default parameters and a precise docstring that specifies valid input ranges as preconditions.
"""
print("\nEXTENSION 3")

# 3.a
def power_of_2_table(n: int) -> None:
    """
    Print a table of powers of 2, from 2^0 to 2^n.

    Parameters
    ----------
    n : int
        Highest exponent to print.

    Returns
    -------
    None
    """
    for i in range(n + 1):
        print(f'2^{i} = {pow(2, i)}')

# 3.b
def power_table(base: float, n: int) -> None:
    """
    Print a table of powers of a given base, from base^0 to base^n.

    Parameters
    ----------
    base : float
        Base to raise to each power.
    n : int
        Highest exponent to print.

    Returns
    -------
    None
    """
    for i in range(n + 1):
        print(f'{base}^{i} = {pow(base, i)}')

# 3.c
def power_table(base: float, start: int, end: int, step: int) -> None:
    """
    Print a table of powers of a given base, from base^start to base^end in increments of step.

    Parameters
    ----------
    base : float
        Base to raise to each power.
    start : int
        First exponent to print.
    end : int
        Last exponent to print (inclusive).
    step : int
        Increment between consecutive exponents.

    Returns
    -------
    None
    """
    for i in range(start, end + 1, step):
        print(f'{base}^{i} = {pow(base, i)}')

# 3.d
"""
i)   Only the 'base' and 'end' parameters.
ii)  'start' and 'step', with defaults '= 0' and '= 1' respectively.
iii) The function becomes less immediately intuitive to use, and callers who only need the simple case have to think about parameters they don't actually care about.
"""

# 3.e
def power_table(base: float, end: int, start: int = 0, step: int = 1) -> None:
    """
    Print a table of powers of a given base.

    Parameters
    ----------
    base : float
        Base to raise to each power.
    end : int
        Last exponent to print (inclusive). Must be >= start.
    start : int, optional
        First exponent to print (default is 0).
    step : int, optional
        Increment between consecutive exponents (default is 1). Must be a positive integer.

    Returns
    -------
    None
        The function only prints the power table; it returns nothing.
    """
    for i in range(start, end + 1, step):
        print(f'{base}^{i} = {pow(base, i)}')
power_table(5, 5)


# Extension 4 - Dead code and defensive programming
"""
Tasks:
a. Write a function called safe_log(x, base) that computes log_base(x) using math.log(x) / math.log(base).
b. Add input validation that handles:
   - x <= 0 (logarithm undefined)
   - base <= 0 or base == 1 (invalid base)
   - base or x are not numeric types (wrong type)
   For each invalid case, print a specific error message. Uses a GUARD CLAUSE pattern.
c. Write a test block that calls safe_log with:
   - safe_log(100, 10)
"""
print("\nEXTENSION 4")

# 4.a
def safe_log(x: float, base: float) -> float:
    """
    Compute the logarithm of x in the given base.

    Parameters
    ----------
    x : float
        Value to take the logarithm of.
    base : float
        Logarithm base.

    Returns
    -------
    float
        log_base(x).
    """
    return math.log(x) / math.log(base)

# 4.b
def safe_log(x: float, base: float) -> None:
    """
    Compute and print the logarithm of x in the given base, guarding against invalid input.

    Parameters
    ----------
    x : float
        Value to take the logarithm of. Must be numeric and > 0.
    base : float
        Logarithm base. Must be numeric, > 0, and != 1.

    Returns
    -------
    float
        log_base(x)

    Raises
    ------
    TypeError
        If 'x' or 'base' is not numeric.
    ValueError
        If 'x' <= 0 or if 'base' <=0 or 'base' == 1.
    """
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("x and base must be numeric.")
    if x <= 0:
        raise ValueError("logarithm is undefinied for x <= 0.")
    if base <= 0 or base == 1:
        raise ValueError("base must be greater than 0 and different from 1.")
    print(math.log(x) / math.log(base))

# 4.c
safe_log(100, 10)