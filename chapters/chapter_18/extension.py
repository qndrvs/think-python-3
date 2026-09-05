## EXTENSIONS
import re

# 1. Extension - sets and set algebra as a data tool
"""
a. You have two datasets of customer IDs (simulate with sets of integers):
    customers_jan = {1, 2, 3, 4, 5, 7, 9, 12, 15}
    customers_feb = {2, 4, 6, 8, 9, 10, 12, 14}
   Using ONLY set operators (|, &, -, ^, <=, >=):
   - Find customers who bought in both months (retention)
   - Find customers who bought in Jan but not Feb (churned)
   - Find customers who bought in Feb but not Jan (new acquisitions)
   - Find customers who bought in exactly one month (exclusive buyers)
   - What fraction of Jan customers were retained in Feb?
   Write a function called cohort_analysis(set_a, set_b) that returns a dict with all five results.
b. Write a function called jaccard_similarity(set_a, set_b) that returns the Jaccard index: |A ∩ B| / |A ∪ B|.
   Returns 0.0 if both sets are empty. This is used to measure similarity between documents, recommendation systems, and duplicate detection. Add doctests.
c. Write a function called unique_words_per_sentence(text) that:
   - Splits text into sentences on '.', '!', '?'
   - For each sentence, returns the set of unique lowercase words
   - Returns a list of sets
   Then compute the intersection of ALL sentence sets (words common to all) and the union of ALL sentence sets (all unique words in the text).
d. Write a function called find_common_elements(*lists) that takes any number of lists and returns a set of elements that appear in ALL of them.
   Use set.intersection(*sets) or a reduce pattern with &. find_common_elements([1,2,3], [2,3,4], [3,4,5]) -> {3} Add doctests including the empty case and single-list case.
"""
print("\nEXTENSION 1")

# 1.a
customers_jan: set = {1, 2, 3, 4, 5, 7, 9, 12, 15}
customers_feb: set = {2, 4, 6, 8, 9, 10, 12, 14}
def cohort_analysis(set_a: set, set_b: set) -> dict:
    return {
        "both_months": set_a & set_b,
        "jan_only": set_a - set_b,
        "feb_only": set_b - set_a,
        "exclusive_buyers": set_a ^ set_b,
        "retention_rate": len(set_a & set_b) / len(set_a) if set_a else 0
    }

# 1.b
def jaccard_similarity(set_a: set, set_b: set) -> float:
    """
    Calculate the Jaccard similarity between two sets.

    Parameters
    ----------
    set_a : set
        First set.
    set_b : set
        Second set.

    Returns
    -------
    float
        The Jaccard index, or 0.0 if both sets are empty.

    Examples
    --------
    >>> jaccard_similarity({1, 2, 3}, {2, 3, 4})
    0.3333333333333333
    >>> jaccard_similarity(set(), set())
    0.0
    """
    intersection: set = set_a & set_b
    union: set = set_a | set_b
    return len(intersection) / len(union) if union else 0.0

# 1.c
def unique_words_per_sentence(text: str) -> list[set]:
    sentences: list = re.split(r'[.!?]', text)
    unique_words: list = [set(sentence.lower().split()) for sentence in sentences if sentence]
    return unique_words

# 1.d
def find_common_elements(*lists) -> set:
    """
    Return a set of elements that appear in all provided lists.

    Parameters
    ----------
    *lists : list
        Serie de listas a evaluar.

    Returns
    -------
    set
        Set con los elementos que se repiten en cada lista.

    Examples
    --------
    >>> find_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
    {3}
    >>> find_common_elements()
    set()
    >>> find_common_elements([1, 2, 2, 3])
    {1, 2, 3}
    >>> find_common_elements([1, 2, 3], [])
    set()
    >>> find_common_elements([1, 2, 3], [4, 5, 6])
    set()
    >>> find_common_elements(['a', 'b'], ['b', 'c'], ['b', 'd'])
    {'b'}
    """
    if not lists: return set()
    
    sets: list = [set(lst) for lst in lists]
    return set.intersection(*sets)


# 2. Extension - Comprehensions as a data transformation language
"""
a. Given a list of dicts representing records:
    records = [
        {'name': 'Alice', 'score': 87, 'grade': 'B'},
        {'name': 'Bob',   'score': 92, 'grade': 'A'},
        {'name': 'Carol', 'score': 71, 'grade': 'C'},
        {'name': 'Dave',  'score': 88, 'grade': 'B'},
    ]
   Using ONLY comprehensions (no for loops outside a comprehension):
   - Extract a list of names: ['Alice', 'Bob', ...]
   - Extract names of students with score >= 85
   - Build a dict {name: score} for all students
   - Build a set of unique grades
   - Build a dict {grade: [names]} using a dict comprehension
b. Write a function called transpose_matrix(matrix) that takes a list of lists (rows) and returns the transposed matrix using a nested comprehension:
    [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
   Add input validation: all rows must have the same length. Verify: transpose(transpose(M)) == M for any matrix M.
c. Write a function called cartesian_product(*sequences) that returns a list of all tuples formed by taking one element from each sequence:
    cartesian_product([1,2], ['a','b']) -> [(1,'a'),(1,'b'),(2,'a'),(2,'b')]
   Use a nested list comprehension. Verify: len(result) == product of all sequence lengths. This is the foundation of grid search in hyperparameter tuning (Etapa 1).
"""
print("\nEXTENSION 2")

# 2.a
records: list = [
    {'name': 'Alice', 'score': 87, 'grade': 'B'},
    {'name': 'Bob',   'score': 92, 'grade': 'A'},
    {'name': 'Carol', 'score': 71, 'grade': 'C'},
    {'name': 'Dave',  'score': 88, 'grade': 'B'},
]
names: list = [record['name'] for record in records]
high_scorers: list = [record['name'] for record in records if record['score'] >= 85]
name_to_score: dict = {record['name']: record['score'] for record in records}
unique_grades: set = {record['grade'] for record in records}
grade_to_names: dict = {grade: [record['name'] for record in records if record['grade'] == grade] for grade in unique_grades}

# 2.b
def transpose_matrix(matrix):
    """
    Transpose a matrix (list of lists) and return the result.

    Parameters
    ----------
    matrix : list[list]
        Lista de listas a evaluar.

    Returns
    -------
    list[list]
        Transpuesta de la lista de listas evaluada.
    
    Examples
    --------
    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix: return []
    if not all(isinstance(row, list) for row in matrix): raise ValueError("Input must be a list of lists.")
    if len(matrix[0]) == 0: return [[] for i in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        if len(row) != len(matrix[0]): raise ValueError(f"All rows must have the same length. Row 0 has {len(matrix[0])}, Row {i} has {len(row)}.")

    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

# 2.c
def cartesian_product(*sequences):
    """
    Return a list of all tuples formed by taking one element from each sequence.
    
    Parameters
    ----------
    *sequences : list
        Listas a evaluar

    Returns
    -------
    list[tuple]
        Lista de tuplas que agrupan cada índica de cada lista.
    
    Examples
    --------
    >>> cartesian_product([1, 2], ['a', 'b'])
    [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
    """
    if not sequences: return [()]
    result: list[tuple] = [()]
    for sequence in sequences: result = [(temp + (element,) for temp in result for element in sequence)]
    return result