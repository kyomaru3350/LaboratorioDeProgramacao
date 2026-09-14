def conectar():
    import random

    if random.choice([True, False]):
        raise ConnectionError("Não foi possível conectar.")

    return True


tentativas = 0

while tentativas < 3:

    try:
        conectar()
        print("Conexão realizada com sucesso.")
        break

    except ConnectionError:
        tentativas += 1
        print("Erro na conexão.")
        print("Tentativa:", tentativas)

else:
    print("Falha após 3 tentativas.")