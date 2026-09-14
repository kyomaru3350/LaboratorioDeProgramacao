import traceback


def processar(numero):
    return int(numero) * 2


dados = ["10", "20", "abc", None, "30"]

for dado in dados:

    try:
        resultado = processar(dado)
        print("Resultado:", resultado)

    except (TypeError, ValueError):
        print("Erro ao processar:", dado)
        traceback.print_exc()