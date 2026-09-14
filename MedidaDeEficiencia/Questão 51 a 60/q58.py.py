def calcular_gorjeta(conta):
    return conta * 0.10


valor = float(input("Digite o valor da conta: "))

gorjeta = calcular_gorjeta(valor)

print("Gorjeta:", gorjeta)