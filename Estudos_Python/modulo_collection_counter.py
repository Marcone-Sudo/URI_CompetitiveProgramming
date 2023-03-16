"""
Módulo Collection

--> Counter

Primeiramente vamos conceituar "container".

    Um container é um objeto utilizado para armazenar diferentes objetos e fornecer uma maneira de acessar
    os objetos contidos e iterar sobre eles.

    - Counter = "Contador"


    --> Collections -> Hight performance container datatype
    --> Coleções -> Tipo de dados container de alta performance

    --> Counter : Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido 
    com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade
    de ocorrências desse elemento.

--> Precisamos importar o módulo

from collections import Counter

--> Posso utilizar por exemplo para contar as ocorrẽncias de uma palavra dentro de um texto.

--> É muito útil de ser utilizado quando temos um conjunto muito grande de dados e precisamos filtrar informações
como por exemplo o número de ocorrências de um determinado padrão.

from collections import Counter

lista = [1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,6,7,7,7,7]

print(Counter(lista))

lista = Counter(lista)

# Função para mostrar ocorrências mais comuns

"""

