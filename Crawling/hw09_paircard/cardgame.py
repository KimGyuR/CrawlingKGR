from card import Card
from player import Player
from gamedealer import GameDealer

def play_game():
    player1 = Player('알파')
    player2 = Player('베타')

    dealer = GameDealer()

    first = int(input('카드 나누어 주기: '))

    print(f'[GameDealer] 딜러가 가진 카드 수: {52-(2*first)}')


if __name__ == '__main__':
    play_game()