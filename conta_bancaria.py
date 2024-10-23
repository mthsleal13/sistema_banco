from abc import ABC, abstractmethod

# classe abstrata representando uma conta bancária
class ContaBancaria(ABC):
    def __init__(self, titular, saldo = 0):
        self.__titular = titular
        self.__saldo = saldo
        
    # metodo abstrato que será implementado nas subclasses
    @abstractmethod
    def aplicar_tarifa(self):
        pass
    
    # metodo publico para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depositado: R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}.')
        else:
            print('O valor do deposito deve ser positivo')
    
    # metodo público para sacar dinheiro
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Sacado: R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}.')
        else:
            print('Saldo insuficiente ou valor inválido')
    
    # metodo publico para visualizar o saldo
    def visualizar_saldo(self):
        print(f'O saldo atual de {self.__titular}: R${self.__saldo:.2f}.')
    
    # metodo protegido para acessar o saldo em subclasses
    def _get_saldo(self):
        return self.__saldo
    
    # metodo protegido para alterar o saldo em subclasses
    def _set_saldo(self, valor):
        self.__saldo = valor