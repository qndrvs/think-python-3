## EXTENSIONS
import math
from typing import Callable

# 1. Extension 1 - Tuples as compound keys and records
"""
a. Write a function called build_coordinate_map(points) where points is a list of (x, y, label) tuples. Return a dictionary that maps each (x, y) tuple to the label. Add doctests.
b. Write a function called find_nearest(points, target) where target is an (x, y) tuple and points is a list of (x, y, label) tuples. Return the (x, y, label) tuple of the point closest to target using Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2). Add doctests.
c. Write a function called group_by_quadrant(points) where points is a list of (x, y) tuples. Return a dictionary mapping each quadrant string ('Q1', 'Q2', 'Q3', 'Q4', 'origin', 'x_axis', 'y_axis') to a list of points in that region. Add doctests.
"""
print("\nEXTENSION 1")

# 1.a
def build_coordinate_map(points: list) -> dict:
    """
    Map a list of (x, y, label) tuples to a dict keyed by (x, y).

    Parameters
    ----------
    points : list
        A list of (x, y, label) tuples.

    Returns
    -------
    dict
        A mapping from each (x, y) tuple to its corresponding label.

    Examples
    --------
    >>> build_coordinate_map([(1, 2, 'hi'), (2, 1, 'bye')])
    {(1, 2): 'hi', (2, 1): 'bye'}
    """
    result: dict = {}
    for i in points: result[i[:2]] = i[2]
    return result

# 1.b
def find_nearest(points: list, target: tuple) -> tuple:
    """
    Find the point closest to a target coordinate, using Euclidean distance.

    Parameters
    ----------
    points : list
        A list of (x, y, label) tuples.
    target : tuple
        The (x, y) coordinate to measure distances against.

    Returns
    -------
    tuple
        The (x, y, label) tuple from 'points' closest to 'target'.

    Examples
    --------
    >>> find_nearest([(1, 2, 'hi'), (3, 1, 'bye')], (1, 1))
    (1, 2, 'hi')
    """
    x, y = target
    min_d: float | None = None
    nearest: tuple = tuple()
    for i in points:
        x1, y1 = i[:2]
        distance: float = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if min_d is None or distance < min_d:
            min_d = distance
            nearest = i
    return nearest

# 1.c
def group_by_quadrant(points: list) -> dict:
    """
    Group a list of (x, y) points by which quadrant, axis, or origin they fall in.

    Parameters
    ----------
    points : list
        A list of (x, y) tuples.

    Returns
    -------
    dict
        A mapping from each region label ('Q1', 'Q2', 'Q3', 'Q4', 'origin', 'x_axis', 'y_axis') to the list of points in that region.

    Examples
    --------
    >>> group_by_quadrant([(1, 2), (0, 0), (1, 0), (0, 1), (-1, -2), (-1, 1), (2, -1)])
    {'Q1': [(1, 2)], 'Q2': [(-1, 1)], 'Q3': [(-1, -2)], 'Q4': [(2, -1)], 'origin': [(0, 0)], 'x_axis': [(0, 1)], 'y_axis': [(1, 0)]}
    >>> group_by_quadrant([(1, 2), (3, 1)])
    {'Q1': [(1, 2), (3, 1)], 'Q2': [], 'Q3': [], 'Q4': [], 'origin': [], 'x_axis': [], 'y_axis': []}
    """
    result: dict = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': [], 'origin': [], 'x_axis': [], 'y_axis': []}
    marc: dict = {(1, 1): 'Q1', (-1, 1): 'Q2', (-1, -1): 'Q3', (1, -1): 'Q4', (0, 0): 'origin', (0, 1): 'x_axis', (0, -1): 'x_axis', (-1, 0): 'y_axis', (1, 0): 'y_axis'}
    for point in points:
        x, y = point
        x = x / abs(x) if x != 0 else 0
        y = y / abs(y) if y != 0 else 0
        result[marc[(x, y)]].append(point)
    return result


# 2. Extension 2 - zip and enumerate for parallel processing
"""
a. Write a function called dot_product(v1, v2) that computes the dot product of two equal-length lists of numbers Add input validation: both lists must have the same length. Add doctests including the zero case and orthogonal vectors. Geometric note: dot_product([1,0], [0,1]) should be 0.
b. Write a function called vector_add(v1, v2), linear_combination(vectors, coefficients) and vector_scale(v, scalar) using zip and list comprehensions respectively. Return the resulting vector.
c. Write a function called find_differences(list1, list2) that takes two lists of the same length and returns a list of (index, val1, val2) tuples where the values differ. Use enumerate and zip together.
    find_differences([1,2,3], [1,5,3]) -> [(1, 2, 5)]
   Add doctests.
d. Write a function called running_correlation(x_vals, y_vals) that computes the Pearson correlation coefficient between x and y:
    r = sum((xi - x_mean) * (yi - y_mean)) / sqrt(sum((xi - x_mean)^2) * sum((yi - y_mean)^2))
   Use zip to compute the sums. Return 0.0 if either variance is 0.
   Verify: perfectly correlated data ([1,2,3], [2,4,6]) gives r = 1.0.
   Verify: anti-correlated data ([1,2,3], [6,4,2]) gives r = -1.0.
"""
print("\nEXTENSION 2")

# 2.a
def dot_product(v1: list, v2: list) -> float | int:
    """
    Compute the dot product of two equal-length numeric vectors.

    Parameters
    ----------
    v1 : list
        First vector.
    v2 : list
        Second vector.

    Returns
    -------
    float or int
        The dot product of 'v1' and 'v2'.

    Raises
    ------
    ValueError
        If 'v1' and 'v2' don't have the same length.

    Examples
    --------
    >>> dot_product([1,0], [0,1])
    0
    >>> dot_product([0,0], [0,1])
    0
    >>> dot_product([1, 2], [3, 4])
    11
    """
    if len(v1) != len(v2): raise ValueError("Both vectors must have the same length.")
    return sum(a * b for a, b in zip(v1, v2))

# 2.b
def vector_add(v1: list, v2: list) -> list:
    """
    Add two equal-length numeric vectors element-wise.

    Parameters
    ----------
    v1 : list
        First vector.
    v2 : list
        Second vector.

    Returns
    -------
    list
        The element-wise sum of 'v1' and 'v2'.
    """
    return [a + b for a, b in zip(v1, v2)]

def vector_scale(v: list, scalar: float | int) -> list:
    """
    Scale every element of a vector by a constant.

    Parameters
    ----------
    v : list
        The vector to scale.
    scalar : float or int
        The scaling factor.

    Returns
    -------
    list
        'v' with every element multiplied by 'scalar'.
    """
    return [scalar * a for a in v]

def linear_combination(vectors: list, coefficients: list) -> list:
    """
    Compute a linear combination of vectors given their coefficients.

    Parameters
    ----------
    vectors : list
        A list of equal-length numeric vectors.
    coefficients : list
        A list of scalars, one per vector in 'vectors'.

    Returns
    -------
    list
        The vector sum of each vector scaled by its coefficient.

    Raises
    ------
    ValueError
        If 'vectors' is empty.
    """
    if not vectors: raise ValueError("'vectors' must contain at least one vector.")
    result: list = vector_scale(vectors[0], coefficients[0])
    for v, c in zip(vectors[1:], coefficients[1:]):
        result = vector_add(vector_scale(v, c), result)
    return result

# 2.c
def find_differences(list1: list, list2: list) -> list:
    """
    Find the positions where two equal-length lists differ.

    Parameters
    ----------
    list1 : list
        First list.
    list2 : list
        Second list.

    Returns
    -------
    list
        A list of (index, val1, val2) tuples for every index where 'list1' and 'list2' differ.

    Examples
    --------
    >>> find_differences([1, 2, 3], [1, 5, 3])
    [(1, 2, 5)]
    >>> find_differences([1, 1, 1], [1, 1, 1])
    []
    >>> find_differences([1, 2, 3], [4, 5, 6])
    [(0, 1, 4), (1, 2, 5), (2, 3, 6)]
    >>> find_differences([], [])
    []
    """
    return [(index, i, j) for index, (i, j) in enumerate(zip(list1, list2)) if i != j]

# 2.d
def running_correlation(x_vals: list, y_vals: list) -> float:
    """
    Compute the Pearson correlation coefficient between two equal - length numeric sequences.

    Parameters
    ----------
    x_vals : list
        List of x values.
    y_vals : list
        List of y values.

    Returns
    -------
    float
        The Pearson correlation coefficient r, in [-1.0, 1.0]. Returns 0.0 if either 'x_vals' or 'y_vals' has zero variance (or is empty).

    Examples
    --------
    >>> running_correlation([1, 2, 3], [2, 4, 6])
    1.0
    >>> running_correlation([1, 2, 3], [6, 4, 2])
    -1.0
    >>> running_correlation([1, 1, 1], [1, 2, 3])
    0.0
    >>> running_correlation([1, 2, 3], [1, 2, 3])
    1.0
    """
    n = len(x_vals)
    if n == 0:
        return 0.0
    x_mean = sum(x_vals) / n
    y_mean = sum(y_vals) / n
    numerator = 0.0
    sum_sq_x = 0.0
    sum_sq_y = 0.0
    for xi, yi in zip(x_vals, y_vals):
        diff_x = xi - x_mean
        diff_y = yi - y_mean
        numerator += diff_x * diff_y
        sum_sq_x += diff_x ** 2
        sum_sq_y += diff_y ** 2
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    if denominator == 0: return 0.0
    return numerator / denominator


# 3. Extension 3 - Sorting with compound keys
"""
a. Write a function called rank_students(students) where students is a list of (name, grade, age) tuples. Return a new list sorted by:
   - Primary: grade descending
   - Secondary (tie-break): age ascending
   - Tertiary (final tie-break): name alphabetically
   Use sorted() with a key function that returns a tuple. When you return a tuple from key, Python sorts by the first element, then second (for ties), then third. Use negation for descending. Add doctests.
b. Write a function called top_n(items, key_func, n) that returns the top n items from a list according to key_func, in descending order. This is the general pattern for finding extremes. Add doctests.
c. Write a function called sort_by_frequency(items) that takes a list and returns a new list sorted from most to least frequent element, with ties broken by the value itself (ascending).
    sort_by_frequency([3, 1, 4, 1, 5, 9, 2, 6, 5, 5])   ->   [5, 5, 5, 1, 1, 2, 3, 4, 6, 9]
   (5 appears 3 times, 1 appears 2 times, rest appear once)
   Use a frequency dict, then sort with a compound key.
"""
print("\nEXTENSION 3")

# 3.a
def rank_students(students: list) -> list:
    """
    Rank a list of students by grade (descending), breaking ties by age (ascending), then by name (alphabetically).

    Parameters
    ----------
    students : list
        A list of (name, grade, age) tuples.

    Returns
    -------
    list
        A new list of (name, grade, age) tuples, sorted as described above.

    Examples
    --------
    >>> rank_students([("Ana", 9, 14), ("Carlos", 10, 15), ("Beatriz", 10, 14), ("Diego", 9, 13), ("Elena", 10, 15), ("Fernando", 9, 14)])
    [('Beatriz', 10, 14), ('Carlos', 10, 15), ('Elena', 10, 15), ('Diego', 9, 13), ('Ana', 9, 14), ('Fernando', 9, 14)]
    """
    return sorted(
        students,
        key = lambda x: (-x[1], x[2], x[0])
    )

# 3.b
def top_n(items: list, key_func: Callable, n: int) -> list:
    """
    Return the top n items from a list, ranked by key_func in descending order.

    Parameters
    ----------
    items : list
        The list of items to rank.
    key_func : Callable
        A function that extracts a comparison key from each item.
    n : int
        Number of top items to return.

    Returns
    -------
    list
        The top n items, ranked in descending order by key_func.

    Examples
    --------
    >>> top_n([1, 3, 2, 5, 4], key_func = lambda x: x, n = 3)
    [5, 4, 3]
    >>> top_n(['apple', 'pie', 'a'], key_func = len, n = 2)
    ['apple', 'pie']
    >>> top_n([{'val': 10}, {'val': 20}, {'val': 5}], key_func = lambda x: x['val'], n = 1)
    [{'val': 20}]
    >>> top_n([], key_func = lambda x: x, n = 5)
    []
    >>> top_n([1, 2, 3], key_func = lambda x: x, n = 0)
    []
    >>> top_n([10, 20, 30], key_func = lambda x: x, n = 10)
    [30, 20, 10]
    """
    if n <= 0: return []
    return sorted(items, key = key_func, reverse = True)[:n]

# 3.c
def sort_by_frequency(items: list) -> list:
    """
    Sort a list from most to least frequent element, breaking ties by the value itself in ascending order.

    Parameters
    ----------
    items : list
        The list of items to sort.

    Returns
    -------
    list
        A new list sorted by frequency and, for ties, by value.

    Examples
    --------
    >>> sort_by_frequency([3, 1, 4, 1, 5, 9, 2, 6, 5, 5])
    [5, 5, 5, 1, 1, 2, 3, 4, 6, 9]
    >>> sort_by_frequency(['a', 'b', 'b', 'c', 'c', 'c'])
    ['c', 'c', 'c', 'b', 'b', 'a']
    >>> sort_by_frequency([4, 4, 2, 2, 1, 3])
    [2, 2, 4, 4, 1, 3]
    >>> sort_by_frequency([])
    []
    """
    if not items: return []
    frequency: dict = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    sorted_items = sorted(frequency.items(), key = lambda x: (-x[1], x[0]))

    result: list = []
    for value, count in sorted_items:
        result.extend([value] * count)

    return result