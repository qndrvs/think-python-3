## EXERCISES
import random
class Card:
    """Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    def to_tuple(self):
        return (self.suit, self.rank)
    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()
    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()

class Deck:
    def __init__(self, cards):
        self.cards = cards
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                cards.append(card)
        return cards
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def take_card(self):
        return self.cards.pop()
    def put_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()

class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.label = label
        self.cards = []
    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)

# 2. Exercise
class Trick(Deck):
    """Represents a trick in contract bridge."""

    def find_winner(self):
        if not self.cards: return None

        first: Card = self.cards[0]
        first_suit = first.suit

        for card in self.cards[1:]:
            if card.suit == first_suit and card.rank > first.rank: first = card

        return first

# 3. Exercise
class PokerHand(Hand):
    """Represents a poker hand."""

    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter

    def has_flush(self):
        counter: dict = self.get_suit_counts()
        for key, value in counter:
            if value >= 5: return True
            return False

# 4. Exercise
    def has_straight(self):
        if len(self.cards) < 5: return False

        ranks: list = sorted([card.rank for card in self.cards])
        unicos: list = sorted(set(ranks))

        for i in range(len(unicos) - 4):
            window: list = unicos[i:i + 5]
            if all(window[j + 1] - window[j] == 1 for j in range(4)): return True

        return False

# 5. Exercise
    def has_straight_flush(self):
        suits_dict: dict = {}
        for card in self.cards:
            if card.suit not in suits_dict: suits_dict[card.suit] = []
            suits_dict[card.suit].append(card.rank)

        for suit, ranks in suits_dict.items():
            unico: list = sorted(set(ranks))
            if len(unico) < 5: continue

            for i in range(len(unico) - 4):
                window = unico[i:i+5]
                if all(window[j + 1] - window[j] == 1 for j in range(4)): return True

        return False

# 6. Exercise
    def has_pair(self):
        rank_counts: dict = self.get_rank_counts()
        for count in rank_counts.values():
            if count >= 2: return True       
        return False

# 7. Exercise
    def has_full_house(self):
        rank_counts: dict = self.get_rank_counts()
        counts: list = list(rank_counts.values())
        
        has_trips = False
        has_pair = False
        
        for count in counts:
            if count >= 3: has_trips = True
            elif count >= 2: has_pair = True
                
        return has_trips and has_pair

# 8. Exercise
class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=None):
        self.name = name
        if contents is None: contents = []
        self.contents = contents

    def __str__(self):
        t: list = [self.name + ' has pouch contents:']
        for obj in self.contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.contents.append(item)