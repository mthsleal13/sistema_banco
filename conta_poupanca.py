from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def aplicar_tarifa(self):
        rendimento = 0.02 * self._get_saldo() # 2% de rendimento sobre o saldo
        self._set_saldo(self._get_saldo() + rendimento)
        print(f'Rendimento de R${rendimento:.2f} aplicado na Conta Poupança.')