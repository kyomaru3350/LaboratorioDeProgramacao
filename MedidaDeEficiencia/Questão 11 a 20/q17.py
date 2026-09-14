count = 0
valor_arrecadado = 0


while True:
    if count == 10:
        break
    count += 1
    valor_cesta = float(input("Digite o valor da cesta: "))
    valor_arrecadado += valor_cesta

print(f"Valor total arrecadado: R${valor_arrecadado:.2f}") 