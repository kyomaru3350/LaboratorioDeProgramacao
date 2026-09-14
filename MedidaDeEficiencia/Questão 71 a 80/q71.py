class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")

    return saldo - valor


saldo = 100
valor = float(input("Digite o valor do saque: "))

try:
    saldo = sacar(saldo, valor)
    print("Novo saldo:", saldo)

except SaldoInsuficienteError as erro:
    print(erro)