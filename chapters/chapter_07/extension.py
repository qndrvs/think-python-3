## EXTENSIONS

# 1. Extension 1 - Counter patterns and data profiling
"""
Tasks:
a. Write a function called char_frequency(text) that returns a dictionary mapping each character (including spaces and punctuation) to its count.
b. Write a function called letter_frequency(text) that counts only alphabetic characters (a-z), case-insensitive. Use lower() and the in operator to filter.
c. Write a function called most_common_letter(text) that returns the letter with the highest frequency. If there is a tie, return the one that comes first alphabetically. Find the max manually.
d. Write a function called frequency_profile(text) that prints a report:
       === Frequency Profile ===
       Total characters : N
       Unique letters   : N
       Most common      : 'x' (N times)
       Least common     : 'x' (N times)
   Use the functions from above. No new imports.

e. Test frequency_profile with the string: "the quick brown fox jumps over the lazy dog" this is a pangram, it contains every letter of the alphabet. Verify that unique letters == 26.
"""
print("\nEXTENSION 1")

# 1.a
"""
This part asks to recognize each CHARACTER, so we treat b != B, and every similar case is handled the same way.
"""
def char_frequency(text: str) -> dict:
    """
    Count how many times each character appears in a string, treating characters as case-sensitive (b != B).

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    dict
        A mapping from each character found in 'text' to its count.
    """
    frequency: dict = {}
    for i in text:
        if not i in frequency.keys():
            frequency[i] = 1
            continue
        frequency[i] = frequency[i] + 1
    return frequency

# 1.b
def letter_frequency(text: str) -> dict:
    """
    Count how many times each alphabetic character appears in a string, case-insensitively.

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    dict
        A mapping from each lowercase letter found in 'text' to its count. Non-alphabetic characters are ignored.
    """
    frequency: dict = {}
    for i in text.lower():
        if not i.isalpha(): continue
        if not i in frequency.keys():
            frequency[i] = 1
            continue
        frequency[i] = frequency[i] + 1
    return frequency

# 1.c
def most_common_letter(text: str) -> list:
    """
    Find the most frequent letter in a string. Ties are broken by alphabetical order (the first matching letter encountered while scanning the lowercased text).

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    list
        A two-element list: [letter, count] for the most common letter.
    """
    frequency: dict = letter_frequency(text)
    keys = list(frequency.keys())
    max_temp = frequency[keys[0]]
    for i in keys:
        if frequency[i] > max_temp:
            max_temp = frequency[i]
    for i in text.lower():
        if not i.isalpha(): continue
        if frequency[i] == max_temp: return [i, max_temp]

# 1.d
def frequency_profile(text: str) -> None:
    """
    Print a frequency report for a string: total character count, number of unique letters, and the most and least common letters.

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    None
    """
    print("=== Frequency Profile ===")
    print("Total characters : " + str(len(text)))
    print("Unique letters   : " + str(len(list(letter_frequency(text)))))
    most_common_list = most_common_letter(text)
    print("Most common      : '" + most_common_list[0] + "' (" + str(most_common_list[1]) + " times)")
    frequency: dict = letter_frequency(text)
    keys = list(frequency.keys())
    min_temp = frequency[keys[0]]
    for i in keys:
        if frequency[i] < min_temp:
            min_temp = frequency[i]
    for i in text.lower():
        if not i.isalpha(): continue
        if frequency[i] == min_temp:
            print("Least common     : '" + i + "' (" + str(min_temp) + " times)")
            break
    return

# 1.e
frequency_profile("the quick brown fox jumps over the lazy dog")


# 2. Extension 2 - File iteration and cumulative statistics
"""
NOTE: This extension requires the words.txt file that the chapter downloads. If you don't have it, use any text file you have locally, or generate a list of strings manually.
Tasks:
a. Write a function called load_word_list(filename) that reads a file and returns a list of words (stripped of whitespace, lowercase).
b. Write a function called count_by_length(word_list) that returns a dictionary mapping each word length to the count of words with that length.
   Example: count_by_length(['a', 'bb', 'cc', 'ddd']) -> {1: 1, 2: 2, 3: 1}
c. Write a function called words_of_length(word_list, n) that returns a list of all words with exactly n letters.
d. Write a function called length_profile(word_list) that prints:
       Length  Count   Example
       1       N       <first word of that length>
       2       N       <first word of that length>
       ...
   Sorted by length. Use count_by_length and words_of_length.
e. Write a function called has_pattern(word, pattern) where pattern is a string of letters and underscores, e.g. '_a_a_a' matches 'banana'.
   Rules:
   - len(word) must equal len(pattern)
   - where pattern has a letter, word must have the same letter
   - where pattern has '_', word can have anything
   Use a for loop with zip (zip works here — look it up if needed) or with range and indexing. Find all words in word_list that match the pattern '_a_a_a'.
"""
print("\nEXTENSION 2")

# 2.a
def load_word_list(filename: str) -> list:
    """
    Read a file and return its words as a list, one per line, stripped of surrounding whitespace and lowercased.

    Parameters
    ----------
    filename : str
        Path to the file to read.

    Returns
    -------
    list
        A list of lowercase words, one per line of the file.
    """
    words: list = []
    for line in open(filename):
        word = line.strip().lower()
        words.append(word)
    return words

# 2.b
def count_by_length(word_list: list) -> dict:
    """
    Count how many words in a list have each possible length.

    Parameters
    ----------
    word_list : list
        A list of words.

    Returns
    -------
    dict
        A mapping from word length to the number of words with that length.
    """
    words: dict = {}
    for i in word_list:
        length = len(i)
        if not length in words.keys():
            words[length] = 1
            continue
        words[length] = words[length] + 1
    return words
# print(count_by_length(['a', 'bb', 'cc', 'ddd']))    -> {1: 1, 2: 2, 3: 1}

# 2.c
def words_of_length(word_list: list, n: int) -> list:
    """
    Filter a list of words down to those with exactly n letters.

    Parameters
    ----------
    word_list : list
        A list of words.
    n : int
        The exact length to filter for.

    Returns
    -------
    list
        All words in 'word_list' with length exactly 'n'.
    """
    words: list = []
    for i in word_list:
        if len(i) == n: words.append(i)
    return words
# print(words_of_length(['a', 'bb', 'cc', 'ddd'], 2)) -> ['ddd']

# 2.d
def length_profile(word_list: list) -> None:
    """
    Print a table showing, for each word length present in 'word_list', the count of words with that length and one example word, sorted by length.

    Parameters
    ----------
    word_list : list
        A list of words.

    Returns
    -------
    None
    """
    print("Length  Count   Example")
    indices_words = count_by_length(word_list)
    keys = list(indices_words.keys())

    for i in range(len(keys) - 1):
        for j in range((len(keys)) - i - 1):
            if keys[j] > keys[j+1]:
                temp = keys[j]
                keys[j] = keys[j+1]
                keys[j+1] = temp

    for i in keys:
        print(str(i) + (" " * (8 - len(str(i)))), end = "")
        print(str(indices_words[i]) + (" " * (8 - len(str(i)))), end = "")
        print(words_of_length(word_list, i)[0])
    return None
# length_profile(["waa", "xdd", "prueba", "a"])

# 2.e
def has_pattern(word: str, pattern: str) -> bool:
    """
    Check whether a word matches a pattern made of letters and underscores, where each underscore matches any character.

    Parameters
    ----------
    word : str
        The word to check.
    pattern : str
        A pattern of the same length as 'word', made of letters (which must match exactly) and underscores (which match anything).

    Returns
    -------
    bool
        True if 'word' matches 'pattern'.
    """
    if not len(word) == len(pattern): return False
    for i, j in zip(word, pattern):
        if j == "_": continue
        if i != j: return False
    return True
print([p for p in load_word_list("data/words.txt") if has_pattern(p, '_a_a_a')])


# 3. Extension 3 - Doctest as a correctness contract
"""
Tasks:
a. Write a function called is_vowel(char) that returns True if char is a vowel (a, e, i, o, u), False otherwise, case-insensitive.
   Write at least 8 doctests that cover:
   - lowercase vowels
   - uppercase vowels
   - consonants
   - digits and punctuation
   - empty string (what SHOULD happen? decide and document it)
   - multi-character strings (what SHOULD happen? decide and document it)
b. Write a function called count_vowels(word) that returns the number of vowel characters in a string. Use is_vowel.
   Write doctests including edge cases:
   - empty string
   - no vowels
   - all vowels
c. Write a function called vowel_ratio(word) that returns the fraction of characters that are vowels. Return 0.0 for empty string. Write doctests. Include at least one case where the expected result is a non-terminating decimal — and explain in a comment why you cannot use == to test it, and what you should use instead.
d. Write a function called is_disemvoweled(word) that returns True if the word contains no vowels. Use count_vowels.
e. Use is_disemvoweled and the word list to find all words in words.txt that contain no vowels and have length >= 4. Print them. There should be a small but non-empty set.
   Comment: why do some of these words have no vowels in English? (Think about which letters can act as vowels in certain contexts.)
"""
print("\nEXTENSION 3")

# 3.a
def is_vowel(char: str) -> bool:
    """
    Check whether a given character is a vowel.

    Parameters
    ----------
    char : str
        The character to evaluate. Must be a single character.

    Returns
    -------
    bool
        True if the character is a vowel (a, e, i, o, u).

    Raises
    ------
    ValueError
        If 'char' is not exactly one character long.
    TypeError
        If 'char' is not a str.

    Examples
    --------
    >>> is_vowel('a')
    True
    >>> is_vowel('A')
    True
    >>> is_vowel('x')
    False
    >>> is_vowel(',')
    False
    >>> is_vowel('')
    ValueError # The string to check must be exactly one character long (at least one).
    >>> is_vowel('abc')
    ValueError # The string to check must be exactly one character long (no more than one).
    """
    if type(char) != str: raise TypeError("Must be a string ('str').")
    if len(char) != 1:
        raise ValueError("Must be exactly one character.")
    return char.lower() in "aeiou"

# 3.b
def count_vowels(word: str) -> int:
    """
    Count the total number of vowels in a word.

    Parameters
    ----------
    word : str
        The word to evaluate.

    Returns
    -------
    int
        The total number of vowels in 'word'.

    Raises
    ------
    TypeError
        If 'word' is not a string ('str').

    Examples
    --------
    >>> count_vowels('')
    0
    >>> count_vowels('xxx')
    0
    >>> count_vowels('aeiou')
    5
    """
    if type(word) != str: raise TypeError("Must be a string ('str').")
    count: int = 0
    for i in word:
        if is_vowel(i): count += 1
    return count

# 3.c
def vowel_ratio(word: str) -> float:
    """
    Compute the ratio of vowels to total characters in a word.

    Parameters
    ----------
    word : str
        The word to evaluate.

    Returns
    -------
    float
        The ratio of vowels to total characters. Returns 0.0 for an
        empty string.

    Raises
    ------
    TypeError
        If 'word' is not a string ('str').

    Examples
    --------
    >>> vowel_ratio('')
    0.0
    >>> vowel_ratio('aexxx')
    0.4
    >>> abs(vowel_ratio('abc') - 0.333333333) < 0.00001
    True
    """
    if type(word) != str: raise TypeError("Must be a string ('str').")
    if not word: return 0.0
    return count_vowels(word) / len(word)

# 3.d
def is_disemvoweled(word: str) -> bool:
    """
    Check whether a word contains no vowels at all.

    Parameters
    ----------
    word : str
        The word to evaluate.

    Returns
    -------
    bool
        True if 'word' contains no vowels.

    Raises
    ------
    TypeError
        If 'word' is not a string ('str').

    Examples
    --------
    >>> is_disemvoweled('')
    True
    >>> is_disemvoweled('xxx')
    True
    >>> is_disemvoweled('aeiou')
    False
    """
    if type(word) != str: raise TypeError("Must be a string ('str').")
    count: int = 0
    for i in word:
        if is_vowel(i): count += 1
    return count == 0

# 3.e
print([p for p in load_word_list("data/words.txt") if is_disemvoweled(p) and len(p) >= 4])
"""
Because of the use of 'y' acting as a vowel in some words, plus a few onomatopoeia-like entries present in the word list.
"""