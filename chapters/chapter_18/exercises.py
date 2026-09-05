## EXERCISES
from collections import Counter, defaultdict

# 2. Exercise
def uses_none(word: str, forbidden: str):
    return not set(word.lower()) & set(forbidden.lower())

# 3. Exercise
def can_spell(letters: str, word: str):
    tile_bag: dict = Counter(letters.lower())
    word_needs: dict = Counter(word.lower())
    return not (word_needs - tile_bag)

# 4. Exercise
class PokerHand:
    "clase solo para poder evitar el error tipográfico, la clase está bien definida en el capítulo 17."
def partition(self):
    hands: dict = defaultdict(PokerHand)
    for card in self.cards:
        hands[card.suit].add_card(card)
    return list(hands.values())

# 5. Exercise
def fibonacci(n: int):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# 6. Exercise
def binomial_coeff(n: int, k: int):
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1))

# 7. Exercise
class Deck:
    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)