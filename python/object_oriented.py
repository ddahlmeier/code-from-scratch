"""Object-oriented programming examples from Cracking the coding
interview Chapter 1"""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


# deck of cards: design data structures for a generic deck of cards


from abc import ABCMeta, abstractmethod


class AbstractCard:
    __metaclass__ = ABCMeta

    @abstractmethod
    def play(self):
        pass


class PlayingCard(AbstractCard):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def play(self):
        print "Playing the %s of %s." % (self.rank, self.suit)


class Joker(AbstractCard):

    def __init__(self):
        self.rank = "Joker"

    def play(self):
        print "Playing the Joker."
