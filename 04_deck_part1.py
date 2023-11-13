import random
import card_01 as card
import cards_action_03 as card_deck

# class Card:
#     pass
#     # TODO: сюда копируем реализацию класса карты из предыдущего задания


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = card_deck.cards

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f'{self.cards}'
        pass

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        hand = []
        for card in self.cards[:x]:
            hand.append(card)
        self.cards = self.cards[x:]
        return hand              
        

    def shuffle(self):
        random.shuffle(self.cards)

if __name__ == "__main__":
    # Создаем колоду
    deck = Deck()
    print(f'Создаем колоду: {deck.cards}\n{len(deck.cards)}')
    
    print('-' * 52)
    
    #3Выводим колоду в формате указанном в основном задании
    print(f'Выводим колоду: {deck.show()}\n{len(deck.cards)}')
    
    print('-' * 52)
    
    # Тусуем колоду
    deck.shuffle()
    print(f'Тусуем колоду: {deck.show()}\n{len(deck.cards)}')
    
    print('-' * 52)
    
    # Возьмем 5 карт "в руку"
    hand = deck.draw(5)
    
    # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
    print(f'Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют: {deck.show()}\n{len(deck.cards)}')
    
    print('-' * 52)
    
    # Выводим список карт "в руке"(список hand)
    print(f'Выводим список карт "в руке": {hand}')
