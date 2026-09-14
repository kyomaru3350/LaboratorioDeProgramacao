def calcular_media(n1, n2, n3):

    if n1 < 0 or n1 > 10:
        raise ValueError("Nota 1 inválida.")

    if n2 < 0 or n2 > 10:
        raise ValueError("Nota 2 inválida.")

    if n3 < 0 or n3 > 10:
        raise ValueError("Nota 3 inválida.")

    return (n1 + n2 + n3) / 3


try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = calcular_media(n1, n2, n3)

    print("Média:", media)

    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

except ValueError as erro:
    print("Erro:", erro)