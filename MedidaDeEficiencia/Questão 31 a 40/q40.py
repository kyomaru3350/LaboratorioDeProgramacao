import random
while True:
    numero = random.randint(1, 100)
    palpite = int(input("Digite o seu palpite do numero (digite -1 para sair): "))

    if palpite == -1:
        break
    if palpite == numero:
        print("Parabens você acertou o numero")
    elif palpite > numero:
        print("O numero que você escolheu é maior que o sorteado")
    else:
        print("O numero que você escolheu é menor que o sorteado")
