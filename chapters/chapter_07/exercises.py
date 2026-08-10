## EXERCISES

# 1. Ask a virtual assistant
"""
In the incorrect version, it checks in each iteration whether the letter is present or not (we want it to be present), and instead of ignoring a non-match and continuing (on the first iteration), it returns FALSE right away without checking the rest — so the function's result ends up depending only on the first character (first iteration).
"""


# 2. Exercise
print("\nEXERCISE 2")
def uses_none(word: str, forbidden: str) -> bool:
    """
    Check whether a word contains none of the forbidden letters.

    Parameters
    ----------
    word : str
        The word to check.
    forbidden : str
        A string of letters that must not appear in 'word'.

    Returns
    -------
    bool
        True if 'word' contains no letters from 'forbidden'.
    """
    for letter in word.lower():
        if letter in forbidden.lower(): return False
    return True
print(uses_none('banana', 'xyz'))
print(uses_none('apple', 'efg'))
print(uses_none('testing', 'test'))


# 3. Exercise
print("\nEXERCISE 3")
def uses_only(word: str, available: str) -> bool:
    """
    Check whether a word uses only letters from a given set.

    Parameters
    ----------
    word : str
        The word to check.
    available : str
        A string of letters that 'word' is allowed to use.

    Returns
    -------
    bool
        True if every letter in 'word' appears in 'available'.
    """
    for letter in word.lower():
        if not letter in available.lower(): return False
    return True
print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))
print(uses_only('testing', 'test'))


# 4. Exercise
print("\nEXERCISE 4")
def uses_all(word: str, required: str) -> bool:
    """
    Check whether a word uses every letter in a required set at least once.

    Parameters
    ----------
    word : str
        The word to check.
    required : str
        A string of letters that must all appear in 'word'.

    Returns
    -------
    bool
        True if every letter in 'required' appears in 'word'.
    """
    for letter in required.lower():
        if not letter in word.lower(): return False
    return True
print(uses_all('banana', 'ban'))
print(uses_all('apple', 'api'))
print(uses_all('testing', 'test'))


# 5. Exercise
print("\nEXERCISE 5")

# 5.1
def check_word(word: str, available: str, required: str) -> bool:
    """
    Check whether a word qualifies according to a simple word-game rule: it must use at least 4 letters from the available set, and must contain the required letter.

    Parameters
    ----------
    word : str
        The word to check.
    available : str
        A string of letters the word may draw from.
    required : str
        A single letter (or substring) that must appear in the word.

    Returns
    -------
    bool
        True if 'word' uses at least 4 letters from 'available' and contains 'required'.
    """
    m = 0
    for letter in word.lower():
        if letter in available.lower(): m += 1
    return (m >= 4) and (required.lower() in word.lower())
print(check_word('color', 'ACDLORT', 'R'))
print(check_word('ratatat', 'ACDLORT', 'R'))
print(check_word('rat', 'ACDLORT', 'R'))
print(check_word('told', 'ACDLORT', 'R'))
print(check_word('bee', 'ACDLORT', 'R'))

# 5.2
def word_score(word: str, available: str) -> int:
    """
    Compute a word's score in a simple word-game scoring rule: 1 point for words shorter than 5 letters, otherwise the word's length plus a 7-point bonus if the word uses every letter in 'available'.

    Parameters
    ----------
    word : str
        The word to score.
    available : str
        A string of letters that, if all used, grant a bonus.

    Returns
    -------
    int
        The computed score.
    """
    points = 0
    if len(word) < 5: return 1
    points += len(word)
    m = 0
    for letter in available.lower():
        if letter in word.lower(): m += 1
    if m == len(available):
        points += 7
    return points
print(word_score('card', 'ACDLORT'))
print(word_score('color', 'ACDLORT'))
print(word_score('cartload', 'ACDLORT'))


# 6. Exercise
print("\nEXERCISE 6")
def uses_all_v2(word: str, required: str) -> bool:
    """
    Alternate implementation of the "uses all required letters" check, built by reusing uses_only with its arguments swapped.

    Parameters
    ----------
    word : str
        The word to check.
    required : str
        A string of letters that must all appear in 'word'.

    Returns
    -------
    bool
        True if every letter in 'required' appears in 'word'.
    """
    return uses_only(required, word)
print("done")


# 7. Exercise
"""
It wasn't necessary — just reading the code beforehand was enough to realize that swapping the order of the arguments is all it takes to get the expected output.
"""


# 8. Exercise
print("\nEXERCISE 8")
def uses_any(word: str, letters: str) -> bool:
    """
    Check whether a word contains at least one letter from a given set.

    Parameters
    ----------
    word : str
        The word to check.
    letters : str
        A string of letters to look for.

    Returns
    -------
    bool
        True if at least one letter in 'letters' appears in 'word'.
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
def uses_all(word: str, required: str) -> bool:
    """
    Check whether a word uses every letter in a required set at least once, built on top of uses_any.

    Parameters
    ----------
    word : str
        The word to check.
    required : str
        A string of letters that must all appear in 'word'.

    Returns
    -------
    bool
        True if every letter in 'required' appears in 'word'.
    """
    for letter in required:
        if not uses_any(word, letter):
            return False
    return True
print("done")