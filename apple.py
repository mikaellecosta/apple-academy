from random import sample

ciclo1 = [
    ["Laura", "Pedro", "João", "Vinicius"],
    ["Carlos", "Maria", "Leonardo", "Ana"],
    ["Daniela", "Marcos", "Wesley", "Luiza"],
    ["Daiane", "Felipe", "Teodoro", "Helena"],
    ["Natalia", "Beatriz", "Eduardo", "Caio"],
]

ciclo2 = [
    ["Teodoro", "Daiane", "Luiza"],
    ["Carlos", "João", "Helena"],
    ["Daniela", "Pedro", "Caio"],
    ["Leonardo", "Maria", "Laura"],
    ["Beatriz", "Marcos", "Vinicius"],
    ["Natalia", "Felipe", "Eduardo"],
    ["Ana", "Wesley"],
]

estudantes = [
    "Ana",
    "Maria",
    "João",
    "Vinicius",
    "Natalia",
    "Marcos",
    "Leonardo",
    "Teodoro",
    "Eduardo",
    "Luiza",
    "Wesley",
    "Carlos",
    "Caio",
    "Daiane",
    "Pedro",
    "Felipe",
    "Laura",
    "Helena",
    "Beatriz",
    "Daniela",
]


def encontrar_participacoes(estudante: str) -> list:
    """Essa função encontra em quais grupos os estudantes já participaram"""
    participacoes = list()
    ciclos = ciclo1 + ciclo2
    for grupo in ciclos:
        if estudante in grupo:
            participacoes.append(grupo)

    return participacoes


def classificar_grupo(grupo: list) -> float:
    """
    Essa função dá nota a um grupo, baseado nas participações
    anteriores dos estudantes envolvidos. Pra cada repetição em grupos,
    ou seja, pra cada estudante que já trabalhou com outro anteriormente,
    estamos deduzindo um ponto pra nota final do grupo.
    """
    grupo = grupo.copy()
    nota = 100

    for estudante in grupo:
        # Na linha abaixo, capturamos todas as participações do estudante
        participacoes = encontrar_participacoes(estudante)

        # Na linha abaixo, pegamos apenas os outros estudantes do grupo
        grupo.remove(estudante)

        for participacao in participacoes:
            for outro_estudante in grupo:
                if outro_estudante in participacao:
                    nota = nota - 1

    return nota


def gerador_de_grupos(estudantes: list, tamanho: int, grupos: list):
    """
    Essa função recebe uma lista de estudantes e retorna grupos. Esses
    grupos são de um tamanho especificado, sendo o último grupo será
    composto pelos membros restantes da lista de estudantes.
    """

    # Cria um grupo de 3 ou 4 estudantes
    grupo = sample(estudantes, tamanho)
    # Testa se o grupo gerado tem nota 100

    if classificar_grupo(grupo) == 100:
        # Adiciona o grupo gerado aos grupos
        grupos.append(grupo)
        # Remove esses estudantes agrupados da lista de estudantes
        for estudante in grupo:
            estudantes.remove(estudante)

    # Se o tamanho da lista de estudantes for menor que o tamanho esperado
    if len(estudantes) < tamanho:
        grupos.append(estudantes)
        return grupos
    else:
        # Chame a função de novo
        return gerador_de_grupos(estudantes, tamanho, grupos)


if __name__ == "__main__":
    # print(encontrar_participacoes("Daniela"))
    # print(classificar_grupo(["Daniela", "Pedro", "Laura"]))
    print(gerador_de_grupos(estudantes, 2, []))
