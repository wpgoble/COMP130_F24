from cards import *

class Player:
    hand = []
    money:int
    name:str

    def __init__(self, name, money = 500_000):
        self.name = name
        self.money = money

    def wager(self, amount):
        if self.money - amount >= 0:
            self.money = self.money - amount

    def win(self, amount):
        self.money = self.money + amount

class Poker:
    players = []

    def __init__(self):
        num_players = int(input("How many players? "))
        for i in range(num_players):
            name = input(f"What is the name of Player {i + 1}? ")
            new_player = Player(name)
            self.players.append(new_player)

name = input("What is your name? ")
player1 = Player(name)

the_deck = Deck()
my_hand = []
for i in range(2):
    my_hand.append(the_deck.draw())

print("My Hand:", my_hand)
the_table = []
the_deck.draw()
for i in range(3):
    the_table.append(the_deck.draw())

print("The Table:", the_table)
response = input("Do you want to keep playing?")
if response == "no":
    print("Game over.")
else:
    the_deck.draw()
    the_table.append(the_deck.draw())
    print("The Table:", the_table)