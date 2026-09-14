def numero_perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        return True
    else:
        return False


numero = int(input("Digite um número: "))

if numero_perfeito(numero):
    print("É um número perfeito.")
else:
    print("Não é um número perfeito.")