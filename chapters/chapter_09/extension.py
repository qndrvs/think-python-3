## EXTENSIONS

# 1. Extesion 1 - String slicing as a data access pattern
"""
a. Run this code and explain the output:
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
   Write an explanation in a comment: why did 'a' change when we only modified 'b'?
b. Write a function called safe_append(lst, value) that appends value to a copy of 'lst' and returns the new list, leaving the original unchanged.
    original = [1, 2, 3] 
    result = safe_append(original, 4)
   After the call, 'original' must still be [1, 2, 3].
c. Write a function called running_average(values) that takes a list of numbers and returns a NEW list where each element i is the average of values[0] through values[i].
    running_average([1, 2, 3, 4])   ->   [1.0, 1.5, 2.0, 2.5]
   Do NOT modify the input list. Verify this with an assertion. Add doctests.
"""
print("\nEXTENSION 1")

# 1.a
a = [1, 2, 3]
b = a
b.append(4)
print(a)
"""
'a' also changes, because 'b' is a reference to 'a' — both names point to the same list object in memory, so mutating it through either name is visible through the other.
"""

# 1.b
def safe_append(lst: list, value) -> list:
    """
    Append a value to a copy of a list, leaving the original list unchanged.

    Parameters
    ----------
    lst : list
        The original list. Not modified by this function.
    value : object
        The value to append.

    Returns
    -------
    list
        A new list equal to 'lst' with 'value' appended at the end.
    """
    new_list: list = lst.copy()
    new_list.append(value)
    return new_list
original: list = [1, 2, 3]
result: list = safe_append(original, 4)

# 1.c
def running_average(values: list) -> list:
    """
    Return a new list where each element i is the average of values[0] through values[i].

    Parameters
    ----------
    values : list
        A list of numeric values. Not modified by this function.

    Returns
    -------
    list
        ((values[0]) / 1, (values[0] + values[1]) / 2, ... , (values[0] + ... + values[i]) / (i + 1))

    Examples
    --------
    >>> running_average([1, 2, 3, 4])
    [1.0, 1.5, 2.0, 2.5]
    """
    new_list: list = []
    temp_total: float = 0.0
    for i in range(len(values)):
        temp_total += values[i]
        new_list.append(temp_total / (i + 1.0))
    return new_list


# 2. Extension 2 - Sorting as a data analysis primitive
"""
Tasks:
a. Write a function called median(values) that returns the median of a list of numbers. Do NOT modify the input list (sort a copy).
   Add doctests including edge cases: single element, two elements, even-length list, odd-length list.
b. Write a function called mode(values) that returns the most frequent element in a list. If there is a tie, return the smallest value. Add doctests.
c. Write a function called quartiles(values) that returns a tuple (Q1, Q2, Q3) where:
   - Q2 is the median of the full sorted list
   - Q1 is the median of the lower half (below Q2, not including Q2 if the list has odd length)
   - Q3 is the median of the upper half (above Q2)
   Use your median() function. Handle lists of length < 4 by returning None with a printed error message. Add doctests for even and odd lengths.
d. Write a function called outliers_iqr(values) that returns a list of values that are outliers by the IQR rule:
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    outlier: value < lower_fence or value > upper_fence
   This is the standard boxplot rule used in exploratory data analysis. Add doctests.
   Verify with the dataset [1, 2, 3, 4, 5, 100]: 100 should be detected as an outlier.
"""
print("\nEXTENSION 2")

# 2.a
def median(values: list) -> int | float:
    """
    Compute the median of a list of numeric values.

    Parameters
    ----------
    values : list
        A list of numeric values. Not modified by this function.

    Returns
    -------
    int or float
        The median of 'values'.

    Examples
    --------
    >>> median([9])
    9
    >>> median([1, 2])
    1.5
    >>> median([1.0, 2.0, 1.5])
    1.5
    >>> median([1, 2, 3, 4])
    2.5
    """
    sort_list: list = sorted(values)
    length: int = len(sort_list)
    half: int = length // 2

    if length % 2 == 0:
        return (sort_list[half - 1] + sort_list[half]) / 2
    else:
        return sort_list[half]

# 2.b
def mode(values: list) -> int | float:
    """
    Find the most frequent element in a list. Ties are broken by returning the smallest value among the most frequent ones.

    Parameters
    ----------
    values : list
        A list of numeric values.

    Returns
    -------
    int or float
        The most frequent value in 'values'.

    Examples
    --------
    >>> mode([9])
    9
    >>> mode([1, 2])
    1
    >>> mode([2.0, 2.0, 1.5])
    2.0
    >>> mode([1, 2, 2, 3, 3, 4])
    2
    """
    frequency: dict = {}
    for value in values:
        if value not in frequency.keys():
            frequency[value] = 1
            continue
        frequency[value] += 1
    possible_keys: list = [key for key, count in frequency.items() if count == max(frequency.values())]
    return min(possible_keys)

# 2.c
def quartiles(values: list) -> tuple:
    """
    Compute the (Q1, Q2, Q3) quartiles of a list of numeric values.

    Parameters
    ----------
    values : list
        A list of numeric values. Must contain at least 4 elements.
        Not modified by this function.

    Returns
    -------
    tuple
        q1 : median of the lower half of the list (excluding q2 if the list has odd length).
        q2 : median of the full list.
        q3 : median of the upper half of the list (excluding q2 if the list has odd length).

    Raises
    ------
    ValueError
        If 'values' has fewer than 4 elements.

    Examples
    --------
    >>> quartiles([1, 2, 3, 4])
    (1.5, 2.5, 3.5)
    >>> quartiles([1, 2, 3, 4, 5])
    (1.5, 3, 4.5)
    """
    sort_list: list = sorted(values)
    length: int = len(sort_list)
    half: int = length // 2

    if length < 4: raise ValueError("The list must have at least 4 elements.")

    q2: int | float = median(sort_list)
    q1: int | float = median(sort_list[:half])
    if length % 2 == 0:
        q3: int | float = median(sort_list[half:])
    else:
        q3: int | float = median(sort_list[half + 1:])

    return (q1, q2, q3)

# 2.d
def outliers_iqr(values: list) -> list:
    """
    Find the outliers in a list of numeric values using the standard IQR (interquartile range) boxplot rule.

    Parameters
    ----------
    values : list
        A list of numeric values. Must contain at least 4 elements.

    Returns
    -------
    list
        The values in 'values' that fall outside
        [Q1 - 1.5*IQR, Q3 + 1.5*IQR].

    Examples
    --------
    >>> outliers_iqr([1, 2, 3, 4, 5, 100])
    [100]
    """
    q1, q2, q3 = quartiles(values)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    return [value for value in values if (value < lower_fence or value > upper_fence)]
print("done")


# 3. Extension 3 - List as a stack and queue
"""
Tasks:
a. Implement a stack using a list with these functions:
   - stack_push(stack, value): appends to the end
   - stack_pop(stack): removes and returns the last element; returns None and prints error if stack is empty
   - stack_peek(stack): returns the last element without removing it
   - stack_is_empty(stack): returns True if the stack has no elements
b. Implement a queue using a list with these functions:
   - queue_enqueue(queue, value): appends to the end
   - queue_dequeue(queue): removes and returns the FIRST element; returns None and prints error if queue is empty
   - queue_peek(queue): returns the first element without removing it
   - queue_is_empty(queue): returns True if the queue has no elements
c. Write a function called is_balanced(expression) that takes a string containing parentheses, brackets, and braces, and returns True if they are correctly matched and nested.
   Examples:
    is_balanced('([]{})')   ->   True
    is_balanced('([)]')     ->   False
    is_balanced('((())')    ->   False
    is_balanced('')         ->   True
d. Write a function called evaluate_rpn(tokens) that evaluates a Reverse Polish Notation (RPN) expression given as a list of strings.
   RPN: operands are pushed to a stack; operators pop two operands, compute the result, and push it back. Supported operators: '+', '-', '*', '/'
   Examples:
    evaluate_rpn(['3', '4', '+'])                                 ->   7.0
    evaluate_rpn(['5', '1', '2', '+', '4', '*', '+', '3', '-'])   ->   14.0
   Add doctests.
"""
print("\nEXTENSION 3")

# 3.a
def stack_push(stack: list, value) -> None:
    """
    Push a value onto the top (end) of a stack, in place.

    Parameters
    ----------
    stack : list
        The stack to modify.
    value : object
        The value to push.

    Returns
    -------
    None
    """
    stack.append(value)
def stack_pop(stack: list):
    """
    Remove and return the value at the top (end) of a stack.

    Parameters
    ----------
    stack : list
        The stack to modify.

    Returns
    -------
    object or None
        The removed top value, or None (with a printed error message) if the stack is empty.
    """
    if stack_is_empty(stack):
        print("'stack' is empty.")
        return None
    return stack.pop()
def stack_peek(stack: list):
    """
    Return the value at the top (end) of a stack without removing it.

    Parameters
    ----------
    stack : list
        The stack to inspect.

    Returns
    -------
    object
        The top value of the stack.
    """
    return stack[-1]
def stack_is_empty(stack: list) -> bool:
    """
    Check whether a stack has no elements.

    Parameters
    ----------
    stack : list
        The stack to check.

    Returns
    -------
    bool
        True if the stack is empty.
    """
    return len(stack) == 0

# 3.b
def queue_enqueue(queue: list, value) -> None:
    """
    Add a value to the back (end) of a queue, in place.

    Parameters
    ----------
    queue : list
        The queue to modify.
    value : object
        The value to add.

    Returns
    -------
    None
    """
    queue.append(value)
def queue_dequeue(queue: list):
    """
    Remove and return the value at the front (start) of a queue.

    Parameters
    ----------
    queue : list
        The queue to modify.

    Returns
    -------
    object or None
        The removed front value, or None (with a printed error message) if the queue is empty.
    """
    if queue_is_empty(queue):
        print("'queue' is empty.")
        return None
    return queue.pop(0)
def queue_peek(queue: list):
    """
    Return the value at the front (start) of a queue without removing it.

    Parameters
    ----------
    queue : list
        The queue to inspect.

    Returns
    -------
    object
        The front value of the queue.
    """
    return queue[0]
def queue_is_empty(queue: list) -> bool:
    """
    Check whether a queue has no elements.

    Parameters
    ----------
    queue : list
        The queue to check.

    Returns
    -------
    bool
        True if the queue is empty.
    """
    return len(queue) == 0

# 3.c
def is_balanced(expression: str) -> bool:
    """
    Check whether all parentheses, brackets, and braces in a string are correctly matched and nested.

    Parameters
    ----------
    expression : str
        The text to evaluate.

    Returns
    -------
    bool
        True if all brackets in 'expression' are correctly matched and nested.

    Examples
    --------
    >>> is_balanced('([]{})')
    True
    >>> is_balanced('([)]')
    False
    >>> is_balanced('((())')
    False
    >>> is_balanced('')
    True
    """
    brackets: dict = {'(' : ')', '{': '}', '[': ']'}
    opens: list = []

    for letter in expression:
        if letter in brackets.values():
            if len(opens) == 0 or letter != brackets[opens.pop()]: return False
        if letter in brackets.keys(): opens.append(letter)
    return stack_is_empty(opens)

# 3.d
def evaluate_rpn(tokens: list) -> float:
    """
    Evaluate a Reverse Polish Notation (RPN) expression.

    Parameters
    ----------
    tokens : list
        A list of strings representing numbers and operators ('+', '-', '*', '/') in RPN order.

    Returns
    -------
    float
        The result of evaluating the expression.

    Raises
    ------
    ZeroDivisionError
        If the expression divides by zero.
    ValueError
        If 'tokens' is malformed (does not reduce to exactly one final value).

    Examples
    --------
    >>> evaluate_rpn(['3', '4', '+'])
    7.0
    >>> evaluate_rpn(['5', '1', '2', '+', '4', '*', '+', '3', '-'])
    14.0
    """
    stack: list = []
    def div(a, b):
        if b == 0: raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": div
    }
    for item in tokens:
        if item in operators.keys():
            b: float = stack.pop()
            a: float = stack.pop()
            result: float = operators[item](a, b)
            stack.append(result)
        else:
            stack.append(float(item))
    if len(stack) != 1: raise ValueError("Malformed 'tokens' input.")
    return stack[0]
print("done")