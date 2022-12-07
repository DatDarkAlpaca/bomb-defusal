from random import randint


class Bomb:
    def __init__(self, password_length: int):
        self.password = []
        self.generate_password(password_length)

    def generate_password(self, password_length: int):
        self.password.clear()
        for index in range(0, password_length):
            self.password.append(randint(0, 9))

    def check_if_entry_is_part_of_password(self, index) -> bool:
        return index in self.password
