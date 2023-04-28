"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanelaTamanhoFixo(ABC):
    
    @abstractmethod
    def mostrar_menu(self):
        pass

    @abstractmethod  
    def fechar(self):
        pass

class IJanelaSemMenu(ABC):
    
    @abstractmethod
    def maximizar(self):
        pass
    
    @abstractmethod
    def minimizar(self):
        pass
    
    @abstractmethod
    def fechar(self):
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


