"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanelaTamanhoFixo(ABC):

    @abstractmethod
    def maximizar(self):
        pass
    
    @abstractmethod
    def minimizar(self):
        pass
    
    @abstractmethod
    def mostrar_menu(self):
        pass

    @abstractmethod  
    def fechar(self):
        pass

class JanelaTamanhoFixo(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass


