## EXERCISES
import re

# 1. Ask a virtual assistant
"""
a.
Metacharacters define the search logic:
- . (Dot): Matches any character except a newline.
- ^ and $: Anchor the pattern to the start and end of the string, respectively.
- * (Asterisk): "0 or more" repetitions quantifier.
- + (Plus): "1 or more" repetitions quantifier.
- ? (Question mark): "0 or 1" quantifier (makes the element optional).
- | (Pipe): Logical "OR" operator (alternation between patterns).
- [] (Brackets): Defines a set of allowed characters (e.g. [aeiou]).
- () (Parentheses): Creates capture groups or groups elements to apply quantifiers.
- \\ (Backslash): Escape character. Introduces special sequences such as:
  * \\d: Digits (0-9)
  * \\w: Word characters (a-z, A-Z, 0-9, _)
  * \\s: Whitespace
  It also neutralizes special characters (e.g. \\. matches a literal dot).

b.
import re

# Pattern for a phone number in XXX-XXX-XXXX format
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"

# Explanation:
# ^            : Start of string
# \d{3}        : Three digits
# -            : A literal hyphen
# \d{3}        : Three digits
# -            : A literal hyphen
# \d{4}        : Four digits
# $            : End of string

# Valid examples: "555-123-4567", "000-000-0000"
# Invalid examples: "5551234567", "55-123-4567", "555-12-4567"

c.
import re

# Pattern for an address: Number + Street name + (ST or AVE)
address_pattern = r"^\d+\s+[A-Za-z]+\s+(?:ST|AVE)$"

# Explanation:
# ^            : Start of string
# \d+          : One or more digits (street number)
# \s+          : One or more whitespace characters
# [A-Za-z]+    : One or more letters (street name)
# \s+          : One or more whitespace characters
# (?:ST|AVE)   : Non-capturing group matching "ST" OR "AVE"
# $            : End of string

# Valid examples: "123 Main ST", "450 Oak AVE"
# Invalid examples: "123 Main Street", "123 ST", "ABC Main ST"

d.
import re

# Pattern for a name with a title (Mr/Mrs) and possible hyphens
name_pattern = r"^(?:Mr|Mrs)\.?\s+(?:[A-Z][a-z]+(?:-[A-Z][a-z]+)?\s*)+$"

# Explanation:
# ^                : Start of string
# (?:Mr|Mrs)       : Required title, "Mr" or "Mrs"
# \.?              : Optional period after the title
# \s+              : Required whitespace
# (?: ... )+       : Repeating group for one or more names
#   [A-Z][a-z]+    : Name starting with an uppercase letter, followed by lowercase
#   (?:-[A-Z][a-z]+)? : Optional hyphenated-name part (e.g. "Mary-Jane")
#   \s*            : Optional whitespace between names
# $                : End of string

# Valid examples: "Mr. John Smith", "Mrs. Mary-Jane Watson", "Mr. Robert Smith-Jones"
# Invalid examples: "John Smith" (no title), "Mr. john" (lowercase), "Ms. Doe" (title not included)

e.
import re

# Robust pattern for URLs (http/https, domains, IPs, ports, paths)
# Note: fully validating URLs per RFC is extremely complex; this pattern covers most practical use cases.
url_pattern = re.compile(
    r'^https?://'  # http or https protocol
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # Domain
    r'localhost|'  # Or localhost
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Or an IPv4 address
    r'(?::\d+)?'  # Optional port (e.g. :8080)
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# Brief explanation:
# - Accepts http:// or https://
# - Validates standard domain names or IP addresses
# - Allows optional ports
# - Accepts trailing paths and query parameters
# - Uses re.IGNORECASE so the domain is case-insensitive

# Valid examples: "https://www.example.com", "http://192.168.1.1:8080/path"
# Invalid examples: "ftp://example.com", "www.example.com" (missing protocol)

f.
RAW STRINGS IN PYTHON

Definition:
A raw string is a string literal prefixed with the letter 'r' or 'R' (example: r"text").

Main purpose:
It tells the Python interpreter to IGNORE escape sequences inside the string. Backslashes ('\\') are treated as literal characters instead of the start of a special code (like \\n for newline or \\t for tab).

Importance in regex:
It's the mandatory standard for writing regular expressions in Python.
- Without 'r': you'd have to manually escape every backslash (e.g. "\\\\d" for a digit).
- With 'r': you write the pattern naturally and readably (e.g. r"\\d").

Comparative example:
  normal_pattern = "\\\\d+\\\\.\\\\d+"   # Hard to read, requires double escaping
  raw_pattern    = r"\d+\.\d+"           # Clean, readable, and functionally identical
"""


# 2. Exercise
print("\nEXERCISE 2")
def head(filename: str, n: int, to_write: str | None = None) -> None:
    """
    Print (or write to a file) the first n lines of a text file.

    Parameters
    ----------
    filename : str
        Path to the input file to read.
    n : int
        Number of lines to read from the start of the file.
    to_write : str or None, optional
        If given, path to a file where the lines are written instead of being printed to the console (default is None, which prints to the console).

    Returns
    -------
    None
    """
    reader = open(filename, encoding = 'utf-8')
    if to_write: writer = open(to_write, 'w')

    main: list = []

    for line, i in zip(reader, range(n)):
        if to_write is None:
            main.append(line)
            continue
        writer.write(line)

    if to_write: writer.close()
    reader.close()

    if main:
        print("".join(main), end = '')
    return
print("done")


# 3. Exercise
print("\nEXERCISE 3")
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
def check_word(word: str) -> bool:
    """
    Check whether a word qualifies as a valid 5-letter answer for this puzzle rule: exactly 5 letters, no letters from a forbidden set, contains 'E', and 'E' is not in positions 3 or 5 (0-indexed 2 or 4).

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if the word satisfies all the rules above.
    """
    if len(word) != 5: return False
    if uses_any(word, 'SPADCLRK'): return False
    word = word.upper()
    if 'E' not in word: return False
    for index, letter in enumerate(word):
        if letter == 'E' and (index in [2, 4]): return False
    return True
print([p.upper() for p in open('data/words.txt') if check_word(p.strip())])


# 4. Exercise
print("\nEXERCISE 4")
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
def check_word(word: str) -> bool:
    """
    Check whether a word qualifies as a valid 5-letter answer for this puzzle rule: exactly 5 letters, contains both 'E' and 'M', no letters from a forbidden set, 'E' is not in positions 3, 4, or 5 (0-indexed 2, 3, 4), and 'M' must be exactly in position 5 (0-indexed 4).

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if the word satisfies all the rules above.
    """
    if len(word) != 5: return False
    word = word.upper()
    if 'E' not in word or 'M' not in word: return False
    if uses_any(word, 'SPADCLRK'): return False
    for index, letter in enumerate(word):
        if letter == 'E' and (index in [2, 3, 4]): return False
        if letter == 'M' and (not index in [4]): return False
    return True
print([p.upper() for p in open('data/words.txt') if check_word(p.strip())])


# 5. Exercise
print("\nEXERCISE 5")
reader = open('data/pg345.txt', encoding = 'utf-8')
pattern = r'\b(?:pale(?:s|d|ness)?|pallor)\b'
bad_words: list = []
for line in reader:
    search = re.findall(pattern, line, re.IGNORECASE)
    if search:
        bad_words.extend(search)
print(bad_words)