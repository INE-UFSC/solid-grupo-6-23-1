"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod


class IJanela(ABC):

    @abstractmethod  
    def fechar(self):
        pass

class IJanelaSemMenu(IJanela, ABC):

    @abstractmethod
    def maximizar(self):
        pass

    @abstractmethod
    def minimizar(self):
        pass

class IJanelaTamanhoFixo(IJanela, ABC):

    @abstractmethod
    def mostrar_menu(self):
        pass

class JanelaTamanhoFixo(IJanelaTamanhoFixo):

    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaSemMenu):

    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass


