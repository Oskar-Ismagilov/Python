from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cloth_cons(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_cons(self):
        return 2 * self.h + 0.3

    def total_cons(self, list):
        sum = 0
        for suit in list:
            sum += suit.cloth_cons
        return sum


coat = Coat(32)
suit_1 = Suit(1.96)
suit_2 = Suit(1.64)
suit_3 = Suit(1.82)
list_suits = [suit_1, suit_2, suit_3]
print(coat.cloth_cons)
print(suit_1.cloth_cons)
print(suit_1.total_cons(list_suits))
