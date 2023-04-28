"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse 
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class AnimalWithoutLegs(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class AnimalWithLegs(Animal):
    def __init__(self, name, legs):       
        super().__init__(name)
        self.__legs = legs

    def leg_count(self) -> int:
        return self.__legs

class Lion(AnimalWithLegs):
    def __init__(self):
        super().__init__('lion', 4)

class Snake(AnimalWithoutLegs):
    def __init__(self):
        super().__init__('snake')


def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        if isinstance(animal, AnimalWithLegs):
            count += animal.leg_count()
    return count

#Exemplo de uso
print(animal_leg_count([Lion(), Snake()]))