total_satisfacao = 0
while True:
    satisfacao = float(input("Digite o nivel de satisfação (0 para sair): "))
    if satisfacao == 0:
        break
    total_satisfacao += satisfacao

print(f"A soma total da satisfação é: {total_satisfacao}")