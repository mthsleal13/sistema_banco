from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def aplicar_tarifa(self):
        tarifa = 5.00 #tarifa fixa de R$5,00
        if self._get_saldo() >= tarifa:
            self._set_saldo(self._get_saldo() - tarifa)
            print(f'Tarifa de R${tarifa:.2f} aplicada na Conta Corrente.')
        else:
            print('Saldo insuficiente para aplicar a tarifa.')