import random

numero = random.randint(1, 10)

tentativa = int(input("Digite um número de 1 a 10: "))

if tentativa == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero)