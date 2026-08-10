## EXTENSIONS
import re

# 1. Extesion 1 - String slicing as a data access pattern
"""
Tasks:
a. You receive sensor log entries in this fixed-width format:
   - '2026-07-04 14:32:01 TEMP  +036.7 OK   '
   - '2026-07-04 14:32:02 HUMID +078.2 WARN '
   - '2026-07-04 14:32:03 PRESS +101.3 OK   '
   Fields are at fixed positions:
   - [0:10]  date
   - [11:19] time
   - [20:25] sensor_type (strip whitespace)
   - [26:32] value (convert to float)
   - [33:37] status (strip whitespace)
   Write a function called parse_log_entry(line) that returns a tuple: (date, time, sensor_type, value, status)
   Use only slicing and strip(). No split(). Add doctests.
b. Write a function called filter_warnings(log_lines) that takes a list of log entry strings and returns a list of only the entries with status 'WARN'. Use parse_log_entry.
c. Write a function called average_sensor_value(log_lines, sensor_type) that returns the average value for all entries of a given sensor type. Use parse_log_entry. Return None if no entries match.
d. Write a function called format_report(log_lines) that prints:
   - === Sensor Report ===
     TEMP  : avg=XX.X  min=XX.X  max=XX.X  warnings=N
     HUMID : avg=XX.X  min=XX.X  max=XX.X  warnings=N
     PRESS : avg=XX.X  min=XX.X  max=XX.X  warnings=N
"""
print("\nEXTENSION 1")

# 1.a
def parse_log_entry(line: str) -> tuple:
    """
    Parse a fixed-width sensor log entry into its individual fields.

    Parameters
    ----------
    line : str
        A single log entry, in the fixed-width format described above.

    Returns
    -------
    tuple
        (date, time, sensor_type, value, status), with 'value' already converted to float and the other fields stripped of surrounding whitespace.

    Raises
    ------
    TypeError
        If 'line' is not a str.

    Examples
    --------
    >>> parse_log_entry('2026-07-04 14:32:01 TEMP  +036.7 OK   ')
    ('2026-07-04', '14:32:01', 'TEMP', 36.7, 'OK')
    >>> parse_log_entry('2026-07-04 14:32:02 HUMID +078.2 WARN ')
    ('2026-07-04', '14:32:02', 'HUMID', 78.2, 'WARN')
    >>> parse_log_entry('2026-07-04 14:32:03 PRESS +101.3 OK   ')
    ('2026-07-04', '14:32:03', 'PRESS', 101.3, 'OK')
    """
    if type(line) != str: raise TypeError("'line' must be a string (str).")

    date: str = line[0:10]
    time: str = line[11:19]
    sensor_type: str = line[20:25].strip()
    value: float = float(line[26:32])
    status: str = line[33:37].strip()
    return (date, time, sensor_type, value, status)

# 1.b
def filter_warnings(log_lines: list) -> list:
    """
    Filter a list of log entries down to those with status 'WARN'.

    Parameters
    ----------
    log_lines : list
        A list of raw log entry strings.

    Returns
    -------
    list
        The subset of 'log_lines' whose status field equals 'WARN'.
    """
    warnings: list = []
    for line in log_lines:
        if parse_log_entry(line)[4] == 'WARN': warnings.append(line)
    return warnings

# 1.c
def average_sensor_value(log_lines: list, sensor_type: str) -> float | None:
    """
    Compute the average value across all log entries of a given sensor type.

    Parameters
    ----------
    log_lines : list
        A list of raw log entry strings.
    sensor_type : str
        The sensor type to filter and average over (e.g. 'TEMP').

    Returns
    -------
    float or None
        The average value of all matching entries, or None if no entries match 'sensor_type'.
    """
    matches: list = []
    for line in log_lines:
        if parse_log_entry(line)[2] == sensor_type: matches.append(line)
    if not matches: return None
    total: float = 0
    for line in matches:
        total += parse_log_entry(line)[3]
    return total / len(matches)

# 1.d
def format_report(log_lines: list) -> None:
    """
    Print a summary report (average, min, max, warning count) for each sensor type present in a list of log entries.

    Parameters
    ----------
    log_lines : list
        A list of raw log entry strings.

    Returns
    -------
    None
    """
    print('=== Sensor Report ===')
    entries_by_type: dict = {'TEMP': [], 'HUMID': [], 'PRESS': []}
    for line in log_lines:
        sensor_type = parse_log_entry(line)[2]
        if sensor_type in entries_by_type:
            entries_by_type[sensor_type].append(line)

    for key in entries_by_type.keys():
        values: list = entries_by_type[key]
        if len(values) == 0: continue   # skip this sensor type, but keep checking the others
        total: float = 0
        warnings: int = 0
        min = max = parse_log_entry(values[0])[3]
        for item in values:
            properties = parse_log_entry(item)
            if min > properties[3]: min = properties[3]
            if max < properties[3]: max = properties[3]
            if properties[4] == 'WARN': warnings += 1
            total += properties[3]
        print(
            str(key) + " " * (5 - len(str(key))) + f' : avg={round(total / len(values), 1)}  min={round(min, 1)}  max={round(max, 1)}  warnings={warnings}'
        )
format_report(['2026-07-04 14:32:03 PRESS +101.3 OK   ', '2026-07-04 14:32:02 HUMID +078.2 WARN ', '2026-07-04 14:32:03 PRESS +101.3 OK   ', '2026-07-04 14:32:01 TEMP  +036.7 OK   '])
print("done")


# 2. Extension 2 - String immutability and the cost of concatenation
"""
Tasks:
a. Write a function called build_string_concat(n) that builds a string of n asterisks by concatenating one at a time.
b. Write a function called build_string_join(n) that builds the same string but collects characters in a list and joins at the end.
c. Explain in a comment WHY concatenation is slower. What does that mean for memory allocation as n grows? This is the difference between O(n) and O(n^2) behavior.
d. Now write a function called reverse_string(s) that returns the reversed string using slice notation. Then write reverse_string_loop(s) that reverses using a for loop and join. Verify both produce identical results for 10 test cases. Which approach is more readable? Which is more Pythonic? Write a comment with your reasoning.
"""
print("\nEXTENSION 2")

# 2.a
def build_string_concat(n: int) -> str:
    """
    Build a string of n asterisks by concatenating one character at a time.

    Parameters
    ----------
    n : int
        Number of asterisks to include.

    Returns
    -------
    str
        A string made of n '*' characters.
    """
    result: str = ''
    for i in range(n):
        result += '*'
    return result

# 2.b
def build_string_join(n: int) -> str:
    """
    Build a string of n asterisks by collecting characters in a list and joining them at the end.

    Parameters
    ----------
    n : int
        Number of asterisks to include.

    Returns
    -------
    str
        A string made of n '*' characters.
    """
    parts: list = []
    for i in range(n):
        parts.append('*')
    return ''.join(parts)

# 2.c
"""
Because of the new objects created: in part a., using '+=' on strings (which are immutable) creates a brand-new string object on every single iteration, copying everything built so far each time — making the code much slower as n grows (this is the O(n^2) behavior, since each of the n concatenations copies an ever-growing string). build_string_join avoids this because a list can grow in place, and the single final join() only copies everything once, giving O(n) behavior overall.
"""

# 2.d
def reverse_string(s: str) -> str:
    """
    Reverse a string using slice notation.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return s[::-1]
def reverse_string_loop(s: str) -> str:
    """
    Reverse a string using a for loop, inserting each character at the front of a list and joining at the end.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    reversed_chars: list = []
    for char in s:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)
"""
The first approach (using s[::-1]) is definitely the more convenient one, since it works directly with the language features and tools Python provides, whereas the loop-based option is a bit more complex to follow and doesn't rely directly on Python's built-in tools.
"""
print("done")


# 3. Extension 3 - Regular expressions as a data filter
"""
Tasks:
a. Write a function called extract_numbers(text) that returns a list of all numbers (integers and floats) found in a string. Use re.findall().
   Test with: 'Temperature: 36.6C, pressure: 101 kPa, delta: -2.3'
   Expected: ['36.6', '101', '-2.3']
b. Write a function called extract_dates(text) that finds all dates in the format YYYY-MM-DD.
   Test with: 'Events on 2026-01-15 and 2026-07-04 were notable.'
c. Write a function called sanitize_id(text) that replaces all sequences of non-alphanumeric characters with a single underscore, and converts to lowercase. Use re.sub().
   sanitize_id('Sensor #3 / Unit A!') -> 'sensor_3_unit_a'
   sanitize_id('  Hello, World! ') -> 'hello_world'
d. Write a function called validate_temperature(text) that returns True if text matches the format: optional sign, 1-3 digits, optional decimal point with 1-2 digits, followed by 'C' or 'F'.
   Examples:
       '36.6C'  -> True
       '-10.5F' -> True
       '100C'   -> True
       '1000C'  -> False  (too many digits)
       '36.6K'  -> False  (wrong unit)
       'warm'   -> False
e. Write a function called find_repeated_words(text) that finds all cases where the same word appears twice in a row (the the, is is). Use re.findall() with a backreference: r'\b(\w+)\s+\1\b'
   Look up what \b and \1 mean in regex — they are not covered in ch8. Test with: 'the the cat sat on on the mat'
   Expected: ['the', 'on']
"""
print("\nEXTENSION 3")

# 3.a
def extract_numbers(text: str) -> list:
    """
    Extract all integer and floating-point numbers found in a string.

    Parameters
    ----------
    text : str
        The text to search.

    Returns
    -------
    list
        A list of matched numbers, as strings (e.g. '36.6', '-2.3').
    """
    pattern: str = r'[-+]?\d+(?:\.\d+)?'
    return re.findall(pattern, text)

# 3.b
def extract_dates(text: str) -> list:
    """
    Extract all dates in YYYY-MM-DD format found in a string.

    Parameters
    ----------
    text : str
        The text to search.

    Returns
    -------
    list
        A list of matched date strings.
    """
    pattern: str = r'\d{4}-\d{2}-\d{2}'
    return re.findall(pattern, text)

# 3.c
def sanitize_id(text: str) -> str:
    """
    Convert a string into a lowercase, underscore-separated identifier by collapsing all non-alphanumeric character sequences into a single underscore.

    Parameters
    ----------
    text : str
        The text to sanitize.

    Returns
    -------
    str
        The sanitized, lowercase identifier.
    """
    pattern: str = r'[^a-z0-9]+'
    return re.sub(pattern, '_', text.lower()).strip("_")

# 3.d
def validate_temperature(text: str) -> bool:
    """
    Check whether a string represents a valid temperature reading: optional sign, 1-3 digits, optional 1-2 decimal digits, followed by 'C' or 'F'.

    Parameters
    ----------
    text : str
        The text to validate.

    Returns
    -------
    bool
        True if 'text' matches the expected temperature format.
    """
    pattern: str = r'^[-+]?\d{1,3}(?:\.\d{1,2})?[CF]$'
    return bool(re.match(pattern, text))

# 3.e
def find_repeated_words(text: str) -> list:
    """
    Find all words that appear twice in a row (e.g. "the the").

    Parameters
    ----------
    text : str
        The text to search.

    Returns
    -------
    list
        A list of the words found repeated consecutively.
    """
    pattern = r'\b(\w+)\s+\1\b'
    return re.findall(pattern, text)