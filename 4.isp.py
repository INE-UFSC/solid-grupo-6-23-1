"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanela(ABC):
    
    def minimizar(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class IJanelaTamanhoFixo(IJanela):
    
    def mostrar_menu(self):
        raise NotImplementedError

class IJanelaSemMenu(IJanela):

    def maximizar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanelaTamanhoFixo):

    def minimizar(self):
        pass

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


