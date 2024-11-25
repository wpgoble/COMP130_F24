import random

class Card:
    suit:str
    number:str
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self) -> str:
        """string representation
        This method is used to format how we want a specific 
        card to be displayed, for instance if we call print(Card)

        Returns:
            str: card_number of card_suit
        """
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        """Sets how we want the machine readable representation 
        of the Card object. Used for print([Card, Card])

        Returns:
            _type_: card_number of card_suit
        """
        return f"{self.number} of {self.suit}"


class Deck:
    deck:list = []

    def __init__(self):
        face_cards = ["J", "Q", "K", "A"]
        suits = ["♥", "♣", "♠", "♦"]
        for suit in suits:
            for i in range(2, 11):
                temp_card = Card(suit, i)
                self.deck.append(temp_card)
            for face in face_cards:
                temp_card = Card(suit, face)
                self.deck.append(temp_card)
        self.shuffle()

    def shuffle(self) -> None:
        for i in range(len(self.deck)):
            index = random.randint(0, len(self.deck)-1)
            self.deck[i] = self.deck[index]

    def draw(self):
        return self.deck.pop()

if __name__ == "__main__":
    my_deck = Deck()
    my_hand = []
    for i in range(2):
        my_hand.append(my_deck.draw())
    
    print(my_hand)