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

    # def draw_card(self):
    #
    #     c = list.pop(self.cards)
    #     c.show_card()
    #     return c

    def draw_cards(self, amount):
        cards_ = self.cards[:amount]
        self.cards = self.cards[amount:]
        return cards_

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

class Person:
    """docstring for Person."""

    def __init__(self, name, hand):
        super(Person, self).__init__()
        self.name = name
        self.hand = hand

    def count_hand(self):

        hand_value = 0

        for card in self.hand:
            hand_value += CARD_VALUES[card.value]
        return hand_value

    def add_card(self, card):
        self.hand.append(card)
        return

    def show_hand(self):
        for card in self.hand:
            card.show_card()


class Player(Person):
    """docstring for Player."""

    def __init__(self, name, hand):
        super(Player, self).__init__(name, hand)



class Dealer(Person):
    """docstring for Dealer."""

    def __init__(self,  name, hand):
        super(Dealer, self).__init__()
        # self.arg = arg


# class/def ? check_winner

# ręka dealera i gracza

def
    d = Deck()
    d.shuffle()
    # Initial 2 cards for each player
    no_players = 3

    dealer_hand = d.draw_cards(2)
    dealer = Person('Dealer', dealer_hand)
    dealer.show_hand()
    print(f'Dealer\'s cards:{dealer.count_hand()}\n')
    gameon = True
    players = []

    while gameon:

        for number in range (1, no_players+1):

            player_hand = d.draw_cards(2)
            player = Person(f'Player {number}', player_hand)
            player.show_hand()
            print(f'Player {number} cards:{player.count_hand()}\n')

            if player.count_hand() and dealer.count_hand() == 21:
                print(f'Tie! Player {number} and dealer win!')
                gameon = False
                break

            elif player.count_hand() == 21:
                print(f'Blackjack! Player {number} wins!')
                gameon = False
                break

            elif dealer.count_hand() == 21:
                print('Blackjack! Dealer wins!')
                gameon = False
                break

                players.append(player)

                for number in range (1, no_players+1):

                    hit = input(f'Player {number}: Would you like another card? Y/N\n')

                    if hit==('y'):
                        c5 = d.draw_cards(1)
                        players[number].count_hand()
                        print(f'Player {number} hand')
                        players[number].show_hand()
                        print('\n')


if __name__ == '__main__':

                #
                #
                #     if player_hand > 21:
                #         print(f'Your hand is {player_hand}! You loose!')
                #         break
                #
                # elif hit==('n'):
                #     print('Dealer draws:')
                #     c6 = d.draw_card()
                #     dealer_hand +=CARD_VALUES[c6.value]
                #
                #     if dealer_hand > 21:
                #         print(f'Dealer\'s hand is {dealer_hand}! Dealer looses!')
                #         break
                #
                # elif hit==(''):
                #     break
                # else:
                #     print('Please enter y or n from the keyboard')




    # print('Dealer\'s cards:')
    # c1 = d.draw_card()
    # c2 = d.draw_card()
    #
    # dealer_hand = CARD_VALUES[c1.value] + CARD_VALUES[c2.value]
    # # dh = c1
    # print(f'Dealer\'s hand is {dealer_hand}')
    #
    # print('Player\'s cards:')
    # c3 = d.draw_card()
    # c4 = d.draw_card()
    #
    # player_hand = CARD_VALUES[c3.value] + CARD_VALUES[c4.value]
    # print(f'Your hand is {player_hand}')
    #
    #
    # if dealer_hand == 21:
    #     print('Blackjack! Dealer wins!')
    #
    # elif player_hand == 21:
    #     print('Blackjack! You win!')
    #
    # # else:
    #
    # for i in range (0,48):
    #
    #     hit = input('Would you like another card? Y/N\n')
    #
    #     if hit==('y'):
    #         c5 = d.draw_card()
    #         player_hand +=CARD_VALUES[c5.value]
    #
    #
    #
    #         if player_hand > 21:
    #             print(f'Your hand is {player_hand}! You loose!')
    #             break
    #
    #     elif hit==('n'):
    #         print('Dealer draws:')
    #         c6 = d.draw_card()
    #         dealer_hand +=CARD_VALUES[c6.value]
    #
    #         if dealer_hand > 21:
    #             print(f'Dealer\'s hand is {dealer_hand}! Dealer looses!')
    #             break
    #
    #     elif hit==(''):
    #         break
    #     else:
    #         print('Please enter y or n from the keyboard')
