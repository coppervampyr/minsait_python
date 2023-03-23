class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente. Tente novamente")
        else:
            self.saldo -= valor

    def consulta(self):
        print(f"Saldo atual: R${self.saldo: .2f}")