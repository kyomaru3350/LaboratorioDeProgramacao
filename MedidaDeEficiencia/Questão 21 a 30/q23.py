gastos = []

while True:
    gasto = float(input("Digite o gasto do mês (-1 para encerrar): "))
    if gasto == -1:
        break
    gastos.append(gasto)

print(f"A soma dos gastos foi R${sum(gastos):.2f}")