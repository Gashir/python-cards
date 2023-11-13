import card_01 as card
# class Card:
#     pass
#     # TODO: сюда копируем реализацию класса карты из предыдущего задания


cards = []

for suit in card.SUITS[::-1]:
    for val in card.VALUES:
        cards.append(card.Card(val, suit))

# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....


if __name__ == "__main__":
    print(*cards, sep=', ')  