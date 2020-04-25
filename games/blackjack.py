import random


CARD_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
'J':10, 'Q':10, 'K':10, 'A':11} # * 4 colors

CARD_COLORS = ['♥️', '♦️', '♣️', '♠️']

class Card:
    """docstring for Card."""

    def __init__(self, value, color):
        self.value = value
        self.color = color

    # def draw_card(self, value, color):



    def show_card(self):

        print(f'Card is {self.value} {self.color}')
        pass


class Deck:
    """docstring for Deck."""

    def __init__(self):
        super(Deck, self).__init__()
        self.cards = []

        for value in CARD_VALUES.keys():
            for color in CARD_COLORS:
                self.cards.append(Card(value, color))

    def show_deck(self):

        for card in self.cards:
            card.show_card()

    def draw_card(self):

        # c = random.choice(list(self.cards))
        c = self.cards[0]
        c.show_card()
        return c

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards




class Player:
    """docstring for Player."""

    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg

    def print(self):
        print(f'Player\'s turn')



class Dealer:
    """docstring for Dealer."""

    def __init__(self, arg):
            self.arg = arg

# class


if __name__ == '__main__':


    d = Deck()
    d.shuffle()
    d.draw_card()


     # Tu musi być jakaś pętla
    # for i in range (0, 52):
    #
    #     value = random.choice(list(CARD_VALUES))
    #     color = random.choice(list(CARD_COLORS))
    #     c = Card(value, color)
    #     c.show_card()



    # deck jest pomniejszany o właśnie wylosowaną kartę





    # hand = 2 cards from the deck
    # print(c)
