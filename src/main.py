from src.game import Game


def main():
    game = Game({
        'password_length': 4,
        'max_attempts': 4 * 4
    })

    game.run()


if __name__ == '__main__':
    main()
