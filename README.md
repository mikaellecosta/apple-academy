<p align="center">
  <a href="#-objetivo">Objetivo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-pesquisa">Pesquisa</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>


# 🧮 Análise Combinatória com Python
Esse programa foi desenvolvido para o teste técnico da etapa de seleção do Apple Academy IFCE.

# 🔍 Objetivo
O programa tem a função de suprir a necessidade de criar novas equipes a cada novo ciclo do Apple Academy, partindo do pressuposto de que nenhum integrante poderá formar grupo com alguém que já trabalhou em algum ciclo anterior. Dessa forma, a aplicação deverá gerar todas as equipes do próximo ciclo (sem nenhuma repetição) e atendendo a especificação de quantas pessoas a equipe deve ter.

# 📚 Pesquisa
O processo de pesquisa até a solução final do problema foi dado da seguinte forma: análise exploratória de algoritmos clássicos construídos em Python, auxílio da documentação Python 3.10.6 e utilização do livro "Use a cabeça!: Python".

### Bibliográfia:
- https://docs.python.org/pt-br/3.10/index.html
- https://github.com/TheAlgorithms/Python
- BARRY, Paul. Use a Cabeça!: Python. 2° edição. Alta Books, 2018

# 💻 Projeto
Explicação de como cada etapa do código foi desenvolvida:
### Dados Iniciais

``` python
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
    "Ana","Maria","João","Vinicius",
    "Natalia","Marcos","Leonardo","Teodoro",
    "Eduardo","Luiza","Wesley","Carlos",
    "Caio","Daiane","Pedro","Felipe",
    "Laura","Helena","Beatriz","Daniela",
] 
```

A primeira parte foi introduzir o banco de informações que temos dos ciclos anteriores, para que assim o código possa trabalhar a partir de uma base pré-definida. Nesse caso, temos dados do Ciclo 1, Ciclo 2 e nome de todos os estudantes.

### Mapeando os grupos em que um estudante esteve
``` python
def encontrar_participacoes(estudante: str) -> list:
    participacoes = list()
    ciclos = ciclo1 + ciclo2
    for grupo in ciclos:
        if estudante in grupo:
            participacoes.append(grupo)

    return participacoes
 ```
 Essa função permite que seja possível encontrar os grupos que cada estudante participou e guardá-los dentro da variável 'participacoes' para ser usada mais tarde.
 
 ### Avaliando se um grupo é ideal
 ```python
 def classificar_grupo(grupo: list) -> float:
 
    grupo = grupo.copy()
    nota = 100

    for estudante in grupo:
        participacoes = encontrar_participacoes(estudante)

        grupo.remove(estudante)

        for participacao in participacoes:
            for outro_estudante in grupo:
                if outro_estudante in participacao:
                    nota = nota - 1

    return nota
```
Para cada novo grupo criado, essa função irá avaliar se o mesmo segue todas as condições que um grupo ideal deve ter. Dessa forma, baseado nas partipações anteriores contidas na variável 'participacoes' será avaliado se há repetições dentro do grupo, caso haja, a cada estudante realizando grupo com um mesmo integrante de um ciclo passado é diminuido 1 ponto da nota final (100).

### Gerando grupos do novo ciclo
``` python
def gerador_de_grupos(estudantes: list, tamanho: int, grupos: list):
    
    grupo = sample(estudantes, tamanho)
 
    if classificar_grupo(grupo) == 100:
        grupos.append(grupo)
        for estudante in grupo:
            estudantes.remove(estudante)

    if len(estudantes) < tamanho:
        grupos.append(estudantes)
        return grupos
    else:
        return gerador_de_grupos(estudantes, tamanho, grupos)
```
Finalmente, a cereja do bolo. Aqui podemos criar novos grupos baseados nas funções que já utilizamos anteriormente. 

- Primeiro:
a função pega 3 parâmetros: a lista de estudantes com seus respectivos grupos anteriores, o tamanho que os novos grupos formados devem ter e o último é um save para armazenar os grupos criados.

- Segundo:
utilizamos a função 'classificar_grupo' para checar se o grupo é ideal, caso seja, salvamos o grupo para ser mostrado no final da execução. Caso um estudante esteja alocado em um novo grupo, o seu nome será retirado da lista de estudantes para que assim um novo grupo seja gerado (apenas com membros sem grupo até então).

- Terceiro:
verificamos a cada nova formação se o tamanho da lista de estudantes é menor que o tamanho que deve ter em cada novo grupo, se for, será adicionado aos grupos criados a lista de estudantes (o que não é pra ocorrer). Porém, caso esteja tudo funcionando corretamente, a função será chamada novamente no final de cada nova formação.

### Teste Final: Ciclo 3
Como foi especificado, o novo ciclo deverá ser formado por estudantes que trabalharão em duplas para realizar um pair programming. Assim sendo, o teste realizado para essa condição, e também para outras, foram aprovados.
``` python
if __name__ == "__main__":
    print(gerador_de_grupos(estudantes, 2, []))
```


