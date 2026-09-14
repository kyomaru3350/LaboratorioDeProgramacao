vencedores = []

while True:
    vencedor = str(input("Digite o nome do vencedor (digite fim para encerrar): "))
    if vencedor == "fim":
        break
    vencedores.append(vencedor)

vencedores.reverse()
print(f"A lista invertida é : {vencedores}")