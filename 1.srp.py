"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    @property
    def get_name(self):
        return self.name

class BancoDados:
    def __init__(self):
        self.animais = []


    def save(self, animal: Animal):
        self.animais.append(animal)