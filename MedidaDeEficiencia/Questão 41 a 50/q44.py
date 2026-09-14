matriz = [
    [5, 2],
    [8, 4]
]

menor = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero < menor:
            menor = numero

print("Menor valor:", menor)