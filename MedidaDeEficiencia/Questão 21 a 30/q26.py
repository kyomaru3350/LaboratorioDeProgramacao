produtos = ["feijão", "arroz", "macarrão", "carne"]

procurar_produto = int(input("Digite o codigo do produto que deseja procurar: "))
if procurar_produto > len(produtos):
    print("Produto não encontrado")
else:
    produto = produtos[procurar_produto]
    print(f"o produto procurado é : {produto}")