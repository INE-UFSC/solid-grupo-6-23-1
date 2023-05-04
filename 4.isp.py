"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod


class IJanela(ABC):

    @abstractmethod
    def minimizar(self):
        pass

    @abstractmethod  
    def fechar(self):
        pass

class IJanelaSemTamanhoFixo(IJanela):

    @abstractmethod
    def maximizar(self):
        pass

class IJanelaComMenu(IJanela):

    @abstractmethod
    def mostrar_menu(self):
        pass

#Exemplos classes

#tamanho fixo com menu
class JanelaMenuJogo(IJanelaComMenu):

    def minimizar(self):
        pass

    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass


#tamanho alteravel sem menu
class JanelaWeb(IJanelaSemTamanhoFixo):

    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass


