class ProdutoInvalidoError(Exception):
    pass


class ValorInvalidoError(Exception):
    pass


class QuantidadeInvalidaError(Exception):
    pass


def registrar_venda(produto, preco, quantidade):

    if produto == "":
        raise ProdutoInvalidoError("Nome do produto inválido.")

    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero.")

    if quantidade <= 0 or not isinstance(quantidade, int):
        raise QuantidadeInvalidaError("Quantidade inválida.")

    total = preco * quantidade

    venda = {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }

    return venda


def gerar_relatorio(vendas):

    if len(vendas) == 0:
        print("Nenhuma venda realizada.")
        return

    faturamento = 0
    quantidade_vendas = len(vendas)

    produtos = {}

    for venda in vendas:

        faturamento += venda["total"]

        produto = venda["produto"]

        if produto in produtos:
            produtos[produto] += venda["quantidade"]
        else:
            produtos[produto] = venda["quantidade"]

    produto_mais_vendido = max(produtos, key=produtos.get)

    ticket_medio = faturamento / quantidade_vendas

    print("\n----- RELATÓRIO -----")
    print("Quantidade de vendas:", quantidade_vendas)
    print("Produto mais vendido:", produto_mais_vendido)
    print("Faturamento total:", faturamento)
    print("Ticket médio:", ticket_medio)


vendas = []

while True:

    produto = input("\nDigite o nome do produto ou 'fim' para encerrar: ")

    if produto.lower() == "fim":
        break

    try:

        preco = float(input("Digite o preço: "))
        quantidade = int(input("Digite a quantidade: "))

        venda = registrar_venda(produto, preco, quantidade)

    except ProdutoInvalidoError as erro:
        print("Erro:", erro)

    except ValorInvalidoError as erro:
        print("Erro:", erro)

    except QuantidadeInvalidaError as erro:
        print("Erro:", erro)

    except ValueError:
        print("Digite valores numéricos válidos.")

    else:
        vendas.append(venda)
        print("Venda registrada com sucesso.")

    finally:
        print("Processo de cadastro finalizado.")


gerar_relatorio(vendas)