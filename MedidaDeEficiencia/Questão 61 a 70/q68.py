try:
    lucro = float(input("Digite o lucro: "))
    acionistas = int(input("Digite a quantidade de acionistas: "))

    resultado = lucro / acionistas

except ZeroDivisionError:
    print("A quantidade de acionistas não pode ser zero.")

except ValueError:
    print("Digite apenas números.")

else:
    print("Valor para cada acionista:", resultado)