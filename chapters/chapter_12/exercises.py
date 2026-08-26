## EXERCISES
import random
filename: str = 'data/pg43.txt'
def clean_word(word: str) -> str: return word.strip('.’;,-“”:?—‘!()_').lower()
def clean_line(line: str) -> list: return line.replace('-', ' ').split()

# 1. Ask a virtual assistant
"""
a. Can you rewrite this using setdefault?
    def add_bigram(bigram):
        first, second = bigram
        successor_map.setdefault(first, []).append(second)
        
b. What are the differences between large language models like GPT and Markov chain text analysis?

    They are fundamentally different in mechanism, even though they share
    the surface-level goal of "predicting the next word." The key
    differences:

    1. Context order and memory
    A k-th order Markov chain (like your bigram model, which is order 1)
    predicts the next word based only on the last k words. It has no
    notion of anything beyond that fixed window. An LLM like GPT uses a
    transformer architecture with a self-attention mechanism, which lets
    it condition its prediction on the entire context within its context
    window (which can range from thousands to hundreds of thousands of
    tokens), dynamically weighing which parts of that context are
    relevant to each prediction — it's not a fixed window of size k with
    uniform weights.

    2. "State" representation
    In your implementation, the state is literally the tuple of previous
    words (a discrete key in a dictionary). In an LLM, each word/token is
    represented as a learned high-dimensional vector (embedding), and the
    "state" after processing the context is a continuous, distributed
    vector representation — not a discrete key. This lets it capture
    semantic relationships (that "king" and "queen" are related) that a
    bigram frequency table cannot represent at all.

    3. How probabilities are estimated
    Your Markov model computes probabilities by counting observed
    frequencies directly from the corpus (pure frequentist approach, no
    generalization). An LLM learns a function via gradient descent over
    billions of parameters, which generalizes to sequences it never saw
    literally during training, because it learns structural and semantic
    regularities, not just exact co-occurrences.

    4. Training and inference cost
    Building your bigram table is O(n) in the size of the corpus, and
    inference is an O(1) dictionary lookup. Training an LLM requires
    massive computation (GPUs/TPUs for weeks or months), and inference
    requires a full forward pass through the network (matrix
    multiplications across each of the transformer's dozens of layers).

    5. Long-range coherence
    Because of point 1, a low-order Markov model generates text that is
    locally plausible (bigram to bigram it "sounds natural") but globally
    incoherent — it can't maintain a topic, a reference, or complex
    grammatical structure across a paragraph, because it forgets
    everything except the last k words. An LLM can maintain thematic and
    referential coherence across much longer contexts, precisely because
    it attends to the entire context simultaneously.

    Formal relationship: in fact, LLMs can be seen as a massive
    generalization of Markov chains — both are, at bottom, models that
    define a probability distribution over the next word conditioned on
    what came before. The difference isn't conceptual at that level, but
    in how that conditional distribution is approximated and
    parameterized: a table of discrete counts vs. a deep neural network
    with attention.
"""


# 2. Exercise
trigram_counter: dict = {}
window: list = []

def count_trigram(words: list):
    key: tuple = tuple(words)
    trigram_counter[key] = 1 if key not in trigram_counter else trigram_counter[key] + 1

def process_word_trigram(word: str):
    window.append(word)
    if len(window) == 3:
        count_trigram(window)
        window.pop(0)

reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        process_word_trigram(word)
reader.close()

print(sorted(trigram_counter.items(), reverse = True, key = lambda x: x[1])[:4])


# 3. Exercise
successor_map: dict = {}
window: list = []

def add_trigram(words: list):
    key: tuple = tuple(words[:2])
    if key not in successor_map:
        successor_map[key] = words[2:]
    else:
        successor_map[key].append(words[2])

def process_word_trigram(word: str):
    window.append(word)
    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        process_word_trigram(word)
reader.close()

print(successor_map)


# 4. Exercise
bigram: tuple = random.choice(list(successor_map))
print(' '.join(bigram), end = ' ')
for i in range(47):
    successors: list = successor_map[(bigram)]
    next_word: str = random.choice(successors)
    print(next_word, end = ' ')
    bigram: tuple = (bigram[1], next_word)
print()


# EXTRA
successor_map = {}
window = []
def add_4gram(words: list):
    key: tuple = tuple(words[:3])
    if key not in successor_map:
        successor_map[key] = words[3:]
    else:
        successor_map[key].append(words[3])
def process_word_4gram(word: str):
    window.append(word)
    if len(window) == 4:
        add_4gram(window)
        window.pop(0)
reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        process_word_4gram(word)
reader.close()
trigram_key: tuple = random.choice(list(successor_map))
print(' '.join(trigram_key), end = ' ')
for i in range(46):
    successors: list = successor_map[(trigram_key)]
    next_word: str = random.choice(successors)
    print(next_word, end = ' ')
    trigram_key: tuple = (trigram_key[1], trigram_key[2], next_word)