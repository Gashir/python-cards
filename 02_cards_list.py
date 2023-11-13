import card_01 as card

# class Card:
#     pass
#     # TODO: сюда копируем реализацию класса карты из предыдущего задания


hearts_cards = [card.Card(cards, 'Hearts') for cards in card.VALUES]
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = [card.Card(cards, 'Diamonds') for cards in card.VALUES[::-1]]
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

print(*hearts_cards, sep=', ')
print('-' * 52)
print(*diamonds_cards, sep=', ')

# Почему ошибка позиционного аргумента
# print(hearts_cards)