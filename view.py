import os

from bomb import Bomb


# Utils:
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def position_text(number: int) -> str:
        if number == 1:
            return '1st'
        elif number == 2:
            return '2nd'
        elif number == 3:
            return '3rd'
        else:
            return f"{number}th"


def display_bomb_information(bomb: Bomb):
    print('-= Small Bomb =-')
    print(f"Password Size: {len(bomb.password)}x units.", end='\n\n')


def display_remaining_attempts(remaining: int):
    pass


def display_bomb(bomb: Bomb, guess_position: int) -> None:
    print('[ ', end='')
    for index, number in enumerate(bomb.password):
        if guess_position > index:
            print(str(number) + ' ', end='')
        else:
            print('* ', end='')

    print(']')


def display_indicator_arrow(guess_position: int) -> None:
    print(' ' * 2, end='')
    print('  ' * guess_position, end='')
    print('^')
