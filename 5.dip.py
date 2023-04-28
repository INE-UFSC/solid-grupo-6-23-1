"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


class Player:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

    def report(self):
        print(f'Name:{self.__name()}')
        print(f'HP:{self.__hp()}')
        print(f'Speed:{self.__speed()}')
