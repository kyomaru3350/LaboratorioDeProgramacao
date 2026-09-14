preco = input("Digite o preço do produto: ")

try:
    preco = float(preco)

except ValueError:
    print("Digite um número válido.")

else:
    desconto = preco * 0.10
    preco_final = preco - desconto

    print("Preço com desconto:", preco_final)