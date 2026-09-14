def buscar_permissao(perfil, indice):
    try:
        return perfil["permissoes"][indice]

    except KeyError:
        return "acesso_restrito"

    except IndexError:
        return "acesso_restrito"


perfil = {
    "nome": "Gustavo",
    "permissoes": ["ler", "editar", "excluir"]
}

print(buscar_permissao(perfil, 1))