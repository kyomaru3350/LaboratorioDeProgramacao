produtos = []
count = 0

while True:
    if count > 5:
        break
    produto = str(input("Digite o nome do produto para adicionar a lista (digite 'sair' para encerrar): "))
    if produto == "sair":
        break
    produtos.append(produto)

print(produtos)