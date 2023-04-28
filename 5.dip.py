"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC, abstractmethod

class Player:
    def __init__(self, name):
        self.stats = PrintPlayerReport(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name
    
    def speed(self):
        return self.__speed

class IPlayerReporter(ABC):
    @abstractmethod
    def __init__(self, player: Player):
        pass

    @abstractmethod
    def report(self):
        pass

class PrintPlayerReport(IPlayerReporter):
    def __init__(self, player: Player):
        self.__player = player

    def report(self):
        print(f'Name:{self.__player.name()}')
        print(f'HP:{self.__player.hp()}')
        print(f'Speed:{self.__player.speed()}')