import random
import itertools

class Deck:
    def __init__(self):
        # cards are represented by an index. Easiest to sort and shuffle.
        self.cardindices = list(range(52))
        # cards are indexed based on suits.
        self.cards = list(itertools.product(['club', 'diamond', 'heart', 'spade'], [*range(2,11), *'JQKA']))
        # dealt can be used to store all the cards that have been dealt
        self.dealt = []
    def shuffle(self):
        random.shuffle(self.cardindices)
    def sort(self):
        self.cardindices.sort()
    def deal(self):
        dealcard_i = self.cardindices.pop()
        self.dealt.append(dealcard_i)
        return self.cards[dealcard_i]
    def show_dealt(self):
        for i in self.dealt:
            print(self.cards[i])
    def show_deck(self):
        for i in self.cardindices:
            print(self.cards[i])
    def show_no_of_cards(self):
        return len(self.cardindices)

