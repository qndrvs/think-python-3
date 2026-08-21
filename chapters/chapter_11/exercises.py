## EXERCISES

# 2. Exercise
"""
Are Python tuples always hashable?
Not always. A tuple is hashable if and only if all of its elements are hashable.
- Hashable: t = (1, 2, "hi") -> Yes, it's hashable.
- Not hashable: t = (1, [2, 3]) -> No, because it contains a list.
- Not hashable: t = (1, {"key": "value"}) -> No, because it contains a dict.
"""

# 3. Exercise
def shift_word(word: str, number: int) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    numbers: tuple = range(len(letters))
    letter_map: dict = dict(zip(letters, numbers))
    number_map: dict = dict(zip(numbers, letters))
    result: list = []
    for letter in word:
        temp: int = (letter_map[letter] + number) % 26
        result.append(number_map[temp])
    return ''.join(result)

# 4. Exercise
def most_frequent_letters(text: str) -> str:
    counter: dict = {}
    for letter in text:
        if letter not in counter:
            counter[letter] = 1
            continue
        counter[letter] += 1
    sorted_letters: list = sorted(counter.items(), key = lambda x: x[1], reverse = True)
    return ''.join([value[0] for value in sorted_letters])

# 5. Exercise
def anagrams(words: list) -> list:
    word_dict: dict = {}
    for word in words:
        word_dict[word] = False

    result: list = []
    for word in word_dict:
        anagram: list = []
        if word_dict[word]: continue
        word_dict[word] = True
        word = ''.join(sorted(word))
        for possible in word_dict:
            if ''.join(sorted(possible)) == word:
                word_dict[possible] = True
                anagram.append(possible)
        if len(anagram) > 1: result.append(str(anagram))
    return '\n'.join(result)

# 6. Exercise
def word_distance(word1: str, word2: str) -> int:
    count: int = 0
    for i, j in zip(word1, word2):
        if i != j: count += 1
    return count

# 7. Exercise
def are_anagrams(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)
def is_metathesis_pair(word1: str, word2: str) -> bool:
    if not are_anagrams(word1, word2): return False
    differences = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differences += 1
            if differences > 2: return False
    return differences == 2
def find_metathesis_pairs(word_list: list) -> list:
    pairs = []
    n = len(word_list)
    for i in range(n):
        for j in range(i + 1, n):
            word1 = word_list[i].lower()
            word2 = word_list[j].lower()
            if is_metathesis_pair(word1, word2): pairs.append((word1, word2))
    return pairs