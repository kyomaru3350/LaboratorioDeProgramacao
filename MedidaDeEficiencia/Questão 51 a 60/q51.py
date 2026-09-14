temperaturas = []

for i in range(5):
    temperatura = float(input("Digite a temperatura: "))
    temperaturas.append(temperatura)

soma = 0

for temperatura in temperaturas:
    soma += temperatura

media = soma / 5

print("Temperaturas:", temperaturas)
print("Média:", media)

if media >= 18 and media <= 28:
    print("A média está dentro da faixa ideal.")
else:
    print("A média está fora da faixa ideal.")