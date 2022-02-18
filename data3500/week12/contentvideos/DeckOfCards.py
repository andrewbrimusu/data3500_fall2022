# this code is for section 10.5
# I am not naming the file DeckOfCards_sec_10.5.py
# because it is good style to name a file the name of the class
# the file is named DeckOfCards.py not Card.py because
# the Card class is a supporting class to DeckOfCards


import random

class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        
class DeckOfCards():
    def __init__(self, deck=[]):
        self.deck = deck
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit)
            

        


suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

cards = []
for suit in suits:
    for face in faces:
        cards.append(Card(suit, face))
        
deck = DeckOfCards(cards)

deck.print_deck()
deck.shuffle_deck()
print("-------------")
deck.print_deck()


#checkpoint activity

# this is just a fun example demonstration














# solution
# this solution extends DeckOfCards.py meaning if you run it by itself it will not work

sort_deck() was added to class definition above

deck.sort_deck()
print("---------------")
deck.print_deck()



























            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# def main():
#     suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#     faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#     cards = [] # list of card objects
    
#     for s in suits:
#         for f in faces:
#             cards.append(Card(s,f))

#     deck1 = DeckOfCards(cards)
#     deck1.printDeck()
#     print("----------------")
    
#     deck1.shuffleDeck()
#     deck1.printDeck()
    

# main()