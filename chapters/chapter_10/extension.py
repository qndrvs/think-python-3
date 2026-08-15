## EXTENSIONS

# 1. Extesion 1 - Hash table complexity and the lookup cost trap
"""
Tasks:
a. Write a function called build_lookup_dict(word_list) that takes a list of strings and returns a dictionary with each word as a key and True as the value. This is a set-like structure.
b. Write a function called count_common_words(text, word_list) that counts how many words in text also appear in word_list.
   Write TWO versions:
   - count_common_words_list(text, word_list): uses 'word in word_list'
   - count_common_words_dict(text, lookup_dict): uses 'word in lookup_dict'
   Both must return the same result.
c. Explain in a comment: if word_list has N words and text has M words, what is the time complexity of each version in big-O notation?
   - list version: O(?)
   - dict version: O(?)
   This is not asked as a theoretical exercise — compute N and M from your test and verify that the ratio you measured matches the theory.
"""
print("\nEXTENSION 1")

# 1.a
def build_lookup_dict(word_list: list) -> dict:
    word_dict: dict = {}
    for word in word_list:
        word_dict[word] = True
    return word_dict

# 1.b
def count_common_words_list(text, word_list):
    count: int = 0
    for word in word_list:
        if text == word: count += 1
    return count
def count_common_words_dict(text, lookup_dict):
    count: int = 0
    for word in lookup_dict:
        if text == word: count += 1
    return count

# 1.c
"""
- list version: O(n)
- dict version: O(1)
La complejidad de la lista es directamente proporcional a su longitud. Mientras que la del diccionario es de un mismo valor para todos.
"""


# 2. Extension 2 - Inverted index (a core data structure in search engines)
"""
Tasks:
a. You have a collection of "documents" (just strings for now):
    docs = {
       'doc1': 'the cat sat on the mat',
       'doc2': 'the dog sat on the log',
       'doc3': 'the cat chased the dog',
       'doc4': 'a log is not a mat',
    }
   Write a function called build_inverted_index(docs) that returns a dictionary mapping each word to a LIST of document IDs where it appears.
   The list should not contain duplicates (if a word appears twice in the same doc, the doc ID appears only once in the list).
b. Write a function called search(index, query) that takes the inverted index and a single query word and returns the list of documents containing that word, or an empty list if none.
c. Write a function called search_and(index, word1, word2) that returns the list of documents containing BOTH words.
d. Write a function called search_or(index, word1, word2) that returns documents containing EITHER word (union, no duplicates).
e. Write a function called tf_idf_simplified(docs, word) that computes a simplified relevance score for each document:
   - term frequency (tf) = count of word in doc / total words in doc
   - inverse document frequency (idf) = 1 / number of docs containing word
   - score = tf * idf
   Return a list of (doc_id, score) tuples sorted by score descending. Documents not containing the word have score 0 and are excluded. This is the simplest version of the most important ranking formula in IR.
"""
print("\nEXTENSION 2")

# 2.a
docs = {
   'doc1': 'the cat sat on the mat',
   'doc2': 'the dog sat on the log',
   'doc3': 'the cat chased the dog',
   'doc4': 'a log is not a mat',
}
def build_inverted_index(docs: dict) -> dict:
    map_words: dict = {}
    for key in docs:
        words: list = docs[key].split()
        for word in words:
            if word not in map_words:
                map_words[word] = [key]
                continue
            index: list = map_words[word]
            if key not in index: map_words[word].append(key)
    return map_words

# 2.b
def search(index: dict, query: str) -> list:
    return None if len(index[query]) == 0 else index[query]

# 2.c
def search_and(index: dict, word1: str, word2: str) -> list:
    lst_doc1: list = index[word1]
    lst_doc2: list = index[word2]
    return [key for key in lst_doc1 if key in lst_doc2]

# 2.d
def search_or(index: dict, word1: str, word2: str) -> list:
    lst_doc1: list = index[word1]
    lst_doc2: list = index[word2]
    for key in lst_doc2:
        if key not in lst_doc1: lst_doc1.append(key)
    return lst_doc1

# 2.e
def tf_idf_simplified(docs: str, word: str) -> list:
    map_words: dict = build_inverted_index(docs)  
    if not search(map_words, word): return None
    result: list = []
    for doc in docs:
        words: dict = build_lookup_dict(doc)
        tf: float = count_common_words_dict(word, words) / len(words)
        idf: float = 1 / len(search(map_words, word))
        score: float = tf * idf
        result.append(doc, score)
    result.sort(key = lambda x: x[1])
    return result


# 3. Extension 3 - Memoization and dynamic programming
"""
a. The chapter shows fibonacci_memo uses a GLOBAL dictionary (known). This is a bad design — global state causes bugs in larger programs.
   Rewrite it as fibonacci_memo_v2(n, memo=None) where memo is an optional parameter initialized to None, and you create a new dict inside the function if memo is None, then pass it through recursive calls.
   Verify fibonacci_memo_v2(35) == 9227465.
b. Write a memoized function called count_paths(m, n, memo=None) that counts the number of unique paths from the top-left to the bottom-right of an m x n grid, moving only right or down.
   Recurrence:
    count_paths(1, n) = 1  (only one row: go right)
    count_paths(m, 1) = 1  (only one column: go down)
    count_paths(m, n) = count_paths(m-1, n) + count_paths(m, n-1)
   Test: count_paths(3, 3) == 6, count_paths(4, 4) == 20.
   This problem appears in Google and Amazon interviews.
c. Write a memoized function called min_coins(amount, coins, memo=None) that returns the minimum number of coins needed to make the given amount using the given denominations (list of integers).
   Recurrence:
       min_coins(0, coins) = 0
       min_coins(amount, coins) = 1 + min(min_coins(amount - c, coins)
                                          for c in coins if c <= amount)
   Return -1 if the amount cannot be made with the given coins.
   Test: min_coins(11, [1, 5, 6, 9]) == 2  (two 5s? no: 9+... check it)
   Actually verify: what coins make 11 in minimum steps with [1,5,6,9]?
"""

# 3.a
def fibonacci_memo_v2(n: int, memo = None) -> int:
    if memo is None: memo: dict = {}
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fibonacci_memo_v2[n - 1, memo] + fibonacci_memo_v2[n - 2, memo]
    return memo[n]

# 3.b
def count_paths(m, n, memo = None):
    if memo is None: memo = {}
    key = (m, n)
    if key in memo: return memo[key]
    if m == 1 or n == 1: return 1
    memo[key] = count_paths(m - 1, n, memo) + count_paths(m, n - 1, memo)
    return memo[key]

# 3.c
def min_coins(amount, coins, memo = None):
    if memo is None: memo = {}
    if amount in memo: return memo[amount]
    if amount == 0: return 0
    min_count = float('inf')
    for coin in coins:
        if coin <= amount:
            res = min_coins(amount - coin, coins, memo)
            if res != -1:
                min_count = min(min_count, 1 + res)
    result = -1 if min_count == float('inf') else min_count
    memo[amount] = result
    return result