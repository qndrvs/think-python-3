## EXERCISES

# 1. Exercise
"""
a. Why do keys in Python dictionaries have to be hashable?
Dictionary keys must be hashable because Python uses a hash table internally to store and retrieve data efficiently.
- A hashable object has a hash value that never changes during its lifetime and can be compared with other objects.
- Python uses this hash value to quickly locate where a key-value pair is stored in memory.
- If keys were mutable (like lists or dictionaries), their hash could change after insertion, making it impossible for Python to find them later.

b. How do I make a Python set from a list of strings and check whether a string is an element of the set?
You can easily create a set from a list using the set() function. Sets are ideal for fast membership testing because they use hash tables, just like dictionaries.
Why use a set instead of a list for membership testing?
- List membership (in): O(n) time complexity — checks every element.
- Set membership (in): O(1) average time complexity — uses hash table lookup.
"""

# 2. Exercise
def value_counts(text: str) -> dict:
    frequency: dict = {}
    for letter in text:
        frequency[letter] = frequency.get(letter, 0) + 1
    return frequency

# 3. Exercise
def has_duplicates(sequence: str | list) -> bool:
    frequency: dict = {}
    for letter in sequence:
        if (frequency.get(letter, 0) + 1) != 1: return True
    return False

# 4. Exercise
def find_repeats(counter: dict) -> list:
    return [key for key in counter if counter[key] > 1]

# 5. Exercise
def add_counters(counter1: dict, counter2: dict) -> dict:
    result: dict = counter2.copy()
    for key in dict(counter1):
        result[key] = counter2.get(key, 0) + counter1[key]
    return result

# 6. Exercise
word_list = open('data/words.txt').read().split()
word_dict = {}
for word in word_list:
    word_dict[word] = 1
def is_interlocking(word: str) -> bool:
    first = word[0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict
for word in word_list:
    if len(word) >= 8 and is_interlocking(word):
        first = word[0::2]
        second = word[1::2]
        print(word, first, second)