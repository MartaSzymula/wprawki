import random


CARD_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
'J':10, 'Q':10, 'K':10, 'A':11}

CARD_COLORS = ['♥️', '♦️', '♣️', '♠️']

class Card:
    """docstring for Card."""

    def __init__(self, value, color):
        self.value = value
        self.color = color


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
        c = list.pop(self.cards)
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

# class/def ? check_winner



# ręka dealera i gracza


if __name__ == '__main__':


    d = Deck()
    d.shuffle()

    print('Dealer\'s cards:')
    c1 = d.draw_card()
    c2 = d.draw_card()

    dealer_hand = CARD_VALUES[c1.value] + CARD_VALUES[c2.value]
    # dh = c1
    print(f'Dealer\'s hand is {dealer_hand}')

    print('Player\'s cards:')
    c3 = d.draw_card()
    c4 = d.draw_card()

    player_hand = CARD_VALUES[c3.value] + CARD_VALUES[c4.value]
    print(f'Your hand is {player_hand}')


    if dealer_hand == 21:
        print('Blackjack! Dealer wins!')

    elif player_hand == 21:
        print('Blackjack! You win!')

    # else:

    for i in range (0,48):

        hit = input('Would you like another card? Y/N\n')

        if hit==('y'):
            c5 = d.draw_card()
            player_hand +=CARD_VALUES[c5.value]

            if player_hand > 21:
                print(f'Your hand is {player_hand}! You loose!')
                break
        elif hit==('n'):
            print('Dealer draws:')
            c6 = d.draw_card()
            dealer_hand +=CARD_VALUES[c6.value]

            if dealer_hand > 21:
                print(f'Dealer\'s hand is {dealer_hand}! Dealer looses!')
                break

        elif hit==(''):
            break
        else:
            print('Please enter y or n from the keyboard')


     # Tu musi być jakaś pętla
    # for i in range (0, 52):
        # d.draw_card()
    #
    #     value = random.choice(list(CARD_VALUES))
    #     color = random.choice(list(CARD_COLORS))
    #     c = Card(value, color)
    #     c.show_card()



    # deck jest pomniejszany o właśnie wylosowaną kartę





    # hand = 2 cards from the deck
    # print(c)
