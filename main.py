from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

# criando uma conta corrente e uma conta poupança
conta1 = ContaCorrente('Matheus', 1000)
conta2 = ContaPoupanca('Carol', 2000)

# depositando valores
conta1.depositar(500)
conta2.depositar(300)

# sacando valores
conta1.sacar(200)
conta2.sacar(100)

# aplicar tarifas ou rendimentos
conta1.aplicar_tarifa()
conta2.aplicar_tarifa()

# mostrar saldo final
conta1.visualizar_saldo()
conta2.visualizar_saldo()
