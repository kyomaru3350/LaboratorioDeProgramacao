produtos = {
    1: "Notebook",
    2: "Mouse",
    3: "Teclado"
}


def buscar_produto(id):
    try:
        produto = produtos[id]
        return 200, produto

    except KeyError:
        return 404, "Produto não encontrado"

    except Exception:
        return 500, "Erro interno do servidor"


id = int(input("Digite o ID do produto: "))

status, resposta = buscar_produto(id)

print("Status:", status)
print("Resposta:", resposta)