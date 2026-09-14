while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
        else:
            print("Idade válida:", idade)
            break

    except ValueError:
        print("Digite apenas números.")