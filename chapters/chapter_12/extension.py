## EXTENSIONS
import random
import math
def clean_word(word: str) -> str: return word.strip('.’;,-“”:?—‘!()_').lower()
def clean_line(line: str) -> list: return line.replace('-', ' ').split()

# 1. Extension 1 - Zipf's law: the power law of language
"""
a. Write a function called word_frequencies(filename) that returns a dictionary mapping each word to its frequency, using the same split_line and clean_word approach from the chapter.
b. Write a function called zipf_table(word_counter, top_n=20) that prints a table:
    Rank    Word    Frequency    Expected_ratio    Actual_ratio
    1       the     1614         1.000             1.000
    2       and     972          0.500             0.602
    3       of      941          0.333             0.583
    ...
   Where:
   - Expected_ratio = 1 / rank (Zipf prediction)
   - Actual_ratio = freq / freq_of_rank_1
   Use sorted() with key and reverse=True to get words by frequency.
c. Compute the mean absolute error between expected and actual ratios over the top 20 words. A lower MAE means the text follows Zipf's law more closely. Is this text a good fit?
d. Write a function called hapax_ratio(word_counter) that returns the fraction of unique words that appear exactly once (hapax legomena). In most corpora this is around 40-60% of the vocabulary.
e. Write a function called type_token_ratio(word_counter) that computes:
    TTR = unique_words / total_word_count
   TTR is a measure of lexical diversity. Higher = more varied vocabulary.
"""
print("\nEXTENSION 1")

# 1.a
def word_frequencies(filename: str) -> dict:
    frequency: dict = {}
    for line in open(filename, encoding = 'utf-8'):
        for word in line.replace('-', ' ').split():
            word = word.strip('.’;,-“”:?—‘!()_').lower()
            frequency[word] = 1 if word not in frequency else frequency[word] + 1
    return frequency

# 1.b
def zipf_table(word_counter: dict, top_n: int = 20):
    print('Rank    Word    Frequency    Expected_ratio    Actual_ratio')
    ordered: list = sorted(word_counter.items(), key = lambda x: x[1], reverse = True)
    freq_rank_1: float = ordered[0][1]
    for rank, item in zip(range(top_n), ordered):
        word, freq = item
        rank += 1
        expected_ratio: float = 1.0 / rank
        actual_ratio: float = freq / freq_rank_1
        print(f'{rank:<8}{word:<8}{freq:<13}{expected_ratio:<18.3f}{actual_ratio:<18.3f}')

# 1.c
def calculate_mae(word_counter: dict, top_n: int = 20) -> float:
    ordered: list = sorted(word_counter.items(), key = lambda x: x[1], reverse = True)
    freq_rank_1: float = ordered[0][1]
    total: float = 0.0
    counter: int = 0.0
    for rank, item in zip(range(top_n), ordered):
        freq = item[1]
        rank += 1
        expected_ratio: float = 1.0 / rank
        actual_ratio: float = freq / freq_rank_1
        total += abs(expected_ratio - actual_ratio)
        counter += 1
    return total / counter

# 1.d
def hapax_ratio(word_counter: dict) -> float:
    count: int = 0
    for item in word_counter.items():
        if item[1] == 1: count += 1
    return round(count / len(word_counter), 2)

# 1.e
def type_token_ratio(word_counter: dict) -> float:
    total: int = 0
    for item in word_counter.items():
        total += item[1]
    return round(len(word_counter) / total, 2)


# 2. Extension 2 - Trigram Markov model and text generation
"""
The chapter implements bigram Markov analysis. This extension extends it
to trigrams and adds evaluation metrics.
a. Write a function called build_trigram_successor_map(filename) that maps each (word1, word2) tuple to a list of possible next words. This is more coherent than bigram generation because the model has more context.
b. Write a function called generate_text_trigram(successor_map, n_words=50)
   that generates n_words of text using the trigram model:
   - Start with a random bigram key from successor_map
   - At each step, look up the current bigram, choose a random successor
   - Print the word and advance the bigram window
   - If the current bigram has no successors (end of chain), restart with a random bigram
c. Write a function called perplexity_bigram(test_text, bigram_counter) that estimates how well the bigram model predicts the test text.
   Simplified perplexity:
   - For each consecutive word pair (w1, w2) in test_text:
       - total_bigrams_starting_with_w1 = sum of all bigram counts where first word is w1
       - p(w2 | w1) = bigram_counter.get((w1, w2), 0) / total_count (or epsilon=1e-10 if 0)
       - log_prob += log(p(w2 | w1))  [use math.log]
   - perplexity = exp(-log_prob / N)  [N = number of bigrams evaluated]
   Lower perplexity = better model. This is the standard metric for LMs.
"""
print("\nEXTENSION 2")

# 2.a
window: list = []
def add_trigram(words: list, succ_map: dict):
    key: tuple = tuple(words[:2])
    if key not in succ_map:
        succ_map[key] = words[2:]
    else:
        succ_map[key].append(words[2])

def process_word_trigram(word: str, succ_map: dict):
    window.append(word)
    if len(window) == 3:
        add_trigram(window, succ_map)
        window.pop(0)

def build_trigram_successor_map(filename: str) -> dict:
    successor_map: dict = {}
    for line in open(filename, encoding = 'utf-8'):
        for word in clean_line(line):
            word = clean_word(word)
            process_word_trigram(word, successor_map)
    return successor_map

# 2.b
def generate_text_trigram(successor_map: dict, n_words: int = 50):
    bigram: tuple = random.choice(list(successor_map))
    print(' '.join(bigram), end = ' ')
    for i in range(n_words - 2):
        if bigram not in successor_map: bigram = random.choice(list(successor_map))
        successors: list = successor_map[(bigram)]
        next_word: str = random.choice(successors)
        print(next_word, end = ' ')
        bigram: tuple = (bigram[1], next_word)

# 2.c
def perplexity_bigram(test_text: str, bigram_counter: dict) -> float:
    words = test_text.lower().split()
    N = 0
    log_prob_sum = 0.0
    epsilon = 1e-10
    unigram_counts = {}
    
    for (w1, w2), count in bigram_counter.items():
        if w1 not in unigram_counts:
            unigram_counts[w1] = 0
        unigram_counts[w1] += count
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i+1]
        total_w1 = unigram_counts.get(w1, 0)
        if total_w1 == 0:
            prob = epsilon
        else:
            count_w1_w2 = bigram_counter.get((w1, w2), 0)
            prob = epsilon if count_w1_w2 == 0 else count_w1_w2 / total_w1
        log_prob_sum += math.log(prob)
        N += 1
    if N == 0: return float('inf')
    perplexity = math.exp(-log_prob_sum / N)

    return perplexity


# 3. Extension 3 - N-gram generalization (the real challenge)
"""
a. Write a function called build_ngram_counter(text_words, n) that takes a list of words and an integer n, and returns a dictionary mapping each n-gram tuple to its frequency. This should work for n=1 (unigrams), n=2 (bigrams), n=3 (trigrams), and any n. Use a sliding window of size n.
b. Write a function called build_ngram_successor_map(text_words, n) that builds a successor map where each key is an (n-1)-gram tuple and the value is a list of possible next words. (n=2 gives bigram model, n=3 gives trigram model, etc.)
c. Write a function called generate_text_ngram(successor_map, seed, n_words where seed is a starting (n-1)-gram tuple. Generate n_words of tex following the Markov chain. Handle dead ends by stopping early.
"""
print("\nEXTENSION 3")

# 3.a
def build_ngram_counter(text_words: list, n: int) -> dict:
    frequency: dict = {}
    window: list = []
    for word in text_words:
        window.append(word)
        if len(window) == n:
            key = tuple(window)
            if key not in frequency: frequency[key] = 1
            else: frequency[key] += 1
            window.pop(0)
    return frequency

# 3.b
def build_ngram_successor_map(text_words: list, n: int) -> dict:
    if n == 1: return None
    successors_map: dict = {}
    window: list = []
    for word in text_words:
        window.append(word)
        if len(window) == n:
            key = tuple(window[:n - 1])
            if key not in successors_map:
                successors_map[key] = [window[-1]]
            else:
                successors_map[key].append(window[-1])
            window.pop(0)
    return successors_map

# 3.c
def generate_text_ngram(successor_map: dict, seed: tuple, n_words: int) -> list:
    if not successor_map: return []
    result: list = list(seed)
    current_state: tuple = seed
    words_to_generate: int = n_words - len(seed)
    for i in range(words_to_generate):
        if current_state not in successor_map: break
        possible_next_words: list = successor_map[current_state]
        if not possible_next_words: break
        next_word: str = random.choice(possible_next_words)
        result.append(next_word)
        next_state_list: list = list(current_state[1:])
        next_state_list.append(next_word)
        current_state: tuple = tuple(next_state_list)
    return result