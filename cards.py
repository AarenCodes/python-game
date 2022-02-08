# class Card
    # hold a card
    # know whether it's been matched or not
    # hold the card's location
    # know if two cards are equal or not
    # be able to print out the card
    
class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False
        
        
    def __eq__(self, other):
        return self.card == other.card
    
    def __str__(self):
        return self.card
    
    
if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')
    
    print(card1 == card2)
    print(card1 == card3)
    print(card1)
