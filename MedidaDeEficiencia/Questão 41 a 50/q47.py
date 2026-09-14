matriz = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, -8, -9]
]

quantidade = 0

for linha in matriz:
    for numero in linha:
        if numero > 0:
            quantidade += 1

print("Quantidade de positivos:", quantidade)