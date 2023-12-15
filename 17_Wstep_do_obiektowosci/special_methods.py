# object.__lt__(karta1, other)
#
# object.__le__(karta1, other)
#
# object.__eq__(karta1, other)
#
# object.__ne__(karta1, other)
#
# object.__gt__(karta1, other)
#
# object.__ge__(karta1, other)
#

# object.__len__
#
# object.__iter__
#
# object.__getslice__(karta1,i,j)
#
# object.__add__
#
# object.__sub__
#
# object.__mul__

class IntValue:
    def __init__(self, value):
        self.value = value

    # repr() : evaluatable string representation of an object (can "eval()" it, meaning it is a string representation that evaluates to a Python object)
    def __repr__(self):
        return f"IntValue({self.value})"

    def __gt__(self, other):
        return self.value > other.value


a = IntValue(3)
b = IntValue(5)

b > a  # b.__gt__(a)

b


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        return IntValue(self.value + other.value)


a = IntValue(3)
b = IntValue(5)

a + b

a = IntValue(3)
b = 5

a + b  # error


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        if type(other) == type(self):
            value = other.value
        else:
            value = other
        return IntValue(self.value + value)


a = IntValue(3)
b = 5

a + b  # ok

b + a  # error


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        if type(other) == type(self):
            value = other.value
        else:
            value = other
        return IntValue(self.value + value)

    def __radd__(self, value):
        return IntValue(self.value + value)


a = 3
b = IntValue(5)

a + b
#############################################################
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __len__(self):
        return int(self.length())

    @property
    def r(self):
        return self.length()

    # repr() : evaluatable string representation of an object (can "eval()" it, meaning it is a string representation that evaluates to a Python object)
    # https://docs.python.org/3.11/library/reprlib.html#
    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)


p = Point(3, 4)
len(p)
p


#############################################################

class Card(object):
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    def __init__(self, value='A', suit='spade'):
        self.value, self.suit = value, suit
        print(f"In init; value is {value}; suit is {suit}")
    def __repr__(self):
        return "Card('%s','%s')" % (self.value, self.suit)
    def __gt__(self, other):
        if self.suits.index(self.suit) > self.suits.index(other.suit):
            return True
        if self.suits.index(self.suit) < self.suits.index(other.suit):
            return False
        return self.values.index(self.value) > self.values.index(other.value)


class Card(object):
    def __init__(self, value='A', suit='spade'):
        self.value, self.suit = value, suit
        print(f"In init; value is {value}; suit is {suit}")

    def __repr__(self):
        return "Card('%s','%s')" % (self.value, self.suit)


krol_karo = Card('K', 'diamonds')
as_karo = Card('A', 'diamonds')
dycha_karo = Card('10', 'diamonds')
karty_w_rece = [as_karo, krol_karo, dycha_karo]

karty_w_rece

karty_w_rece.sort()


def moc_karty(karta):
    return len(values) * suits.index(karta.suit) + values.index(karta.value)


moc_karty(krol_karo)
moc_karty(as_karo)
moc_karty(as_karo)

karty_w_rece.sort()

karty_w_rece.sort(key=moc_karty)

karty_w_rece


class Card(object):
    def __init__(self, value='A', suit='spade'):
        self.value, self.suit = value, suit
        print(f"In init; value is {value}; suit is {suit}")

    def __repr__(self):
        return "Card('%s','%s')" % (self.value, self.suit)

    def __eq__(self, card):
        return self.value == card.value and self.suit == card.suit

    def czy_bije(self, other):
        if self.suit == other.suit:
            if values.index(self.value) > values.index(other.value):
                return True
        return False

    def __gt__(self, n):
        return self.czy_bije(n)

    def __lt__(self, card):  # USED IN sort()
        return card.czy_bije(self)


krol_karo = Card('K', 'diamonds')
as_karo = Card('A', 'diamonds')
dycha_karo = Card('10', 'diamonds')
karty_w_rece = [as_karo, krol_karo, dycha_karo]

as_karo.czy_bije(krol_karo)

as_karo > krol_karo

krol_karo < as_karo

as_karo >= krol_karo

karty_w_rece.sort(reverse=True)
karty_w_rece
karty_w_rece.sort()
karty_w_rece

krol_karo1 = Card('K', 'diamonds')
krol_karo2 = Card('K', 'diamonds')
