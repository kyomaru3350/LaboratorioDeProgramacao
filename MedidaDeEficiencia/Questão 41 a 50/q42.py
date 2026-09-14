matriz = [
    [1, 2],
    [3, 4]
]

soma = 0

for linha in matriz:
    for numero in linha:
        soma += numero

print("Soma:", soma)