from view import *


class Game:
    def __init__(self, config: dict):
        self.config = config

        self.bomb = Bomb(config['password_length'])
        self.current_guess = 0
        self.attempts = 0

    def run(self):
        display_bomb_information(self.bomb)

        while True:
            if self.is_winning_condition():
                print('You win!')
                break

            # View:
            display_bomb(self.bomb, self.current_guess)
            display_indicator_arrow(self.current_guess)

            # Input:
            user_input = int(input('Type a number: '))
            cls()

            # Guess Handler:
            display_bomb_information(self.bomb)
            self.guess_flavor_text(user_input)

        print('Final bomb state:')
        display_bomb(self.bomb, self.current_guess)

        self.reset()

    def reset(self):
        self.current_guess = 0
        self.attempts = 0

    def is_winning_condition(self) -> bool:
        return self.current_guess == self.config['password_length']

    def guess_flavor_text(self, user_input):
        guess = self.bomb.password[self.current_guess]

        if user_input == guess:
            print(f"You guessed the {position_text(self.current_guess + 1)} position correctly!")
            self.current_guess += 1

        elif user_input > guess:
            print(f"[ ! ] Your guess ({user_input}) is greater than the {position_text(self.current_guess + 1)} entry!")

        else:
            print(f"[ ! ] Your guess ({user_input}) is smaller than the {position_text(self.current_guess + 1)} entry!")

