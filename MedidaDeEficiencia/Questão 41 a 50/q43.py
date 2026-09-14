matriz = [
    [5, 2],
    [8, 4]
]

maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("Maior valor:", maior)