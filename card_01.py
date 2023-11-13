
# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def to_str(self) -> str:
        return f'{self.value}{SUITS_UNI.get(self.suit)}'
    
    
    def __str__(self) -> str:
        return f'{self.value}{SUITS_UNI.get(self.suit)}'
    def __repr__(self) -> str:
        return self.__str__()
     
    
    def equal_suit(self, other_card) -> bool:
        '''Возвращает True, если у карт одинаковые масти.'''
        
        return bool(self.suit) if self.suit is other_card.suit else False
    
    
    def more(self, other_card) -> bool:
        '''Возвращает True, если карта у которой вызван метод больше, 
        чем карта которую передали в качестве параметра.'''
        
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        else:
            return VALUES.index(self.value) > VALUES.index(other_card.value)   
        
     
    def less(self, other_card) -> bool:
        '''Проверяет является ли карта младше,
            чем карта в параметре.'''
        
        return not Card.more(self, other_card)
        




if __name__ == "__main__":
    # # # Создадим несколько карт
    card1 = Card("10", "Spades")
    card2 = Card("10", "Hearts")
    
    # Выведем карты на экран в виде: 10♥ и A♦
    #print(card1.to_str())
    print("\033[30m{}".format(card1.to_str()))
    print("\033[31m{}".format(card2.to_str()))
    
    print("\033[37m{}".format('-' * 10))
    
    
    
    
    
    
    if card1.more(card2):
        print(f"Kарта: {card1.to_str()} больше карты {card2.to_str()}")
    else:
        print(f"Карта: {card1.to_str()} меньше карты {card2.to_str()}")
        pass
    print('-' * 10)

    if card1.less(card2):
        print(f"Kарта: {card2.to_str()} больше карты {card1.to_str()}")
    else:
        print(f"Карта: {card2.to_str()} меньше карты {card1.to_str()}")
        pass
    
    
    
    print('-' * 10)
    
    # # # Проверим, одинаковые ли масти у карт
    if card1.equal_suit(card2):
        print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
    else:
        print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
        pass
    

#print('\u2661', '\u2665') # Hearts   ♥
#print('\u2662', '\u2666') # Diamonds  ♦
#print('\u2667', '\u2663') # Clubs   ♣
#print('\u2664', '\u2660') # Spades ♠