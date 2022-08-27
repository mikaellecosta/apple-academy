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
] ```

A primeira parte foi introduzir o banco de informações que temos dos ciclos anteriores, para que assim o código possa trabalhar a partir de uma base pré-definida. Nesse caso, temos dados do Ciclo 1, Ciclo 2 e nome de todos os estudantes.

### Mapeando os grupos em que um estudante esteve
``` python
def encontrar_participacoes(estudante: str) -> list:
    """Essa função encontra em quais grupos os estudantes já participaram"""
    participacoes = list()
    ciclos = ciclo1 + ciclo2
    for grupo in ciclos:
        if estudante in grupo:
            participacoes.append(grupo)

    return participacoes
 ```
 Essa função permite que 
