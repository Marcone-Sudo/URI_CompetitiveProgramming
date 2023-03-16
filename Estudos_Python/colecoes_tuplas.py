"""
TUPLAS

As tuplas são imutáveis, ou seja, toda a operação em uma tupla gera uma outra tupla.

As tuplas são representadas por parênteses ()

Caso eu não coloque os parẽnteses o terminal interpreta como uma tupla.

Não existem tuplas com apenas um elemento, sem vírgula.

tupla1 = (2)
tupla2 = (2,)

print(type(tupla1)) --> int
print(type(tupla2)) --> tuple

Conclusão: Tuplas são definidas pelo uso de vírgula

--> Tupla usando range (dinâmicamente)

tupla = tuple(range(10))


--> Desempacotamento de tuplas

nome = ("Marcone", "Marques")
A1, A2 = nome

Segue os mesmos princípios de desempacotamento de listas


--> Métodos para adição e remoção nas tuplas não existem

--> Métodos como len(), sum(), max(), min() são válidos em tuplas

--> Concatenação de tuplas

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2

print(tupla3)


--> Verificar a existência de um elemento em uma tupla

tupla = (1,2,3)
print(3 in tupla)

Será retornado como resposta True

--> Iterando em uma tupla

    --Podemos utilizar o for ou o while para iterar sobre uma tupla
    --No for podemos usar também o enumerate

--> Contando elementos em uma tupla

Utilizamos o método count()

tupla = (1,2,4,56,7,8)
tupla = tupla.count(2)

print(tupla)

--> Dicas de utilização

    - Devemos utilizar tuplas sempre que não precisamos modificar a coleção
    - Podemos utilizar o index() para encontrar a posição de um elemento em uma tupla
    - Tuplas deixam seu código mais seguro, devido a sua imutabilidade.
    - Tuplas são mais rápidas para operações.

--> Copiando uma tupla para outra

tupla = (1,2,4)
nova = tupla

print(nova)

Nas tuplas não temos deep copy, isso se deve pois nas tuplas não podemos adicionar novos elementos


"""