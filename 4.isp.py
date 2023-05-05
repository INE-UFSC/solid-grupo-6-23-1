"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod


class IJanelaFechar(ABC):
    
    @abstractmethod
    def fechar(self):
        pass

class IJanelaTamanhoVariavel(ABC):

    @abstractmethod
    def maximizar(self):
        pass

    @abstractmethod
    def minimizar(self):
        pass

class IJanelaComMenu(ABC):

    @abstractmethod
    def mostrar_menu(self):
        pass

#Exemplos classes
class JanelaTamanhoFixo(IJanelaFechar, IJanelaComMenu):

    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass


#tamanho alteravel sem menu
class JanelaSemMenu(IJanelaFechar, IJanelaTamanhoVariavel):

    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass


