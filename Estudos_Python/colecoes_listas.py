"""
Listas são dinâmicas pois podemos adicionar quantos elementos quisermos, bem como, aceitam qualquer tipo de dados, inclusive outras listas.

--> Em python uma lista é definida pelos colchetes

Definições de listas

nomes = ["", "", ""]  or nomes = list(range(1))

Operações:

--> Podemos encontrar um elemento em uma lista


lista = list(range(10))

if 8 in lista:
    print("OK")
else:
    print("Não encontrei o valor 8")


--> Podemos realizar o ordenamento de elementos dentro de uma lista

Para isso utilizamos o método sort()

Pode ser utilizado para ordenar tipos numéricos. Na ordenação de "strings" a pontuação também é ordenada, veja a ordem que isso ocorre.

1 - Pontuação
2 - Maiúsculas
3 - Minúsculas


num = [1,2,3,22,5,44,3,22,78]

num.sort()
print(num)

--> Podemos contar o número de ocorrências de um elemento em nossa lista.

Para isso utilizamos o método count()

Veja o exemplo:

nome = "Valéria Cristina Fernandes Silva e Dutra"

num_a = nome.count("a")

print(num_a)

--> Podemos adicionar elementos em nossa lista, para isso utilizamos o método append()

A função append() só permite a adição de um elemento por vez.

Vejamos o exemplo.

frutas = ["Maça", "Laranja", "Kiwi"]

print(frutas)

frutas.append("Uva")

print(frutas)

Como vimos podemos adicionar várias estruturas dentro de uma lista, até mesmo outra lista.

lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = []
lista_3.append(lista_1)
lista_3.append(lista_2)
print(lista_3)

--> Podemos adicionar elementos também utilizando para isso o método extend()

Nesse método posso adicionar os elementos de uma lista dentro de uma lista.
    Isso não ocorre com o append()


lista = [0,1,2]
lista.extend([11,12,13])
print(lista)

Obs: Extend não aceita valores únicos

Tanto o append() quanto o extend() adicionam os elementos ao final da lista

--> Para adicionar os elementos em uma posição específica podemos utilizar o método insert()

Lembrando que em uma lista o seu primeiro elemento da esquerda para a direita tem a posição "0", 
caso seja adotado a ordem inversa temos que o valor de índice será "-1"

lista.insert(índice, valor)

numeros = [1,2,3,4,5,7,8]
numeros.insert(5,6)
print(numeros)

--> Concatenando listas

Para juntar duas listas, podemos fazer o seguinte:


lista1 = [1,2,3]
lista2 = [4,5,6]

lista3 = lista1 + lista2

print(lista3)


--> Para inverter uma lista

Para inverter a ordem dos elementos de uma lista podemos utilizar o método reverse()

    Uma outra alternativa é o uso de slice de strings 


numeros = [1,2,3,4,5,6,7,8,9]

print(numeros)

numeros.reverse()

print(numeros)

--> Copiando uma lista

Para copiar uma lista utilizamos o método copy()

--> Para contar o número de elementos de uma lista

Utilizamos o método len()

numeros = [1,2,3,4,5,44,3,2,2,1,234]

print(len(numeros))


--> Para remover o último elemento de uma lista

Utilizamos o método pop()

nome = list(("Marcone de Freitas Marques").split())
print(nome)

nome.pop()

print(nome)

O método pop() além de remover o último elemento da lista também o retorna.

Também podemos passar o índice do elemento que gostaríamos de remover.

nome.pop(indice)

O único cuidado que devemos tomar ao remover um elemento por índice utilizando o método pop() é cuidar para que o índice informado seja válido.


--> Para limpar todos os elementos de uma lista

Podemos utilizar o método clear()

nomes = ["Marcone", "Debora", "Marcos"]

print(nomes)

nomes.clear()

print(nomes)


--> Operações com listas (Multiplicação com listas)

num = list(range(3))
lista = num * 3

print(lista)

Percebe-se que a lista num será repetida 3 vezes como o solicitado


--> Podemos converter uma string em uma lista

nome = "MARCONE"

nome = nome.split()

print(nome)

Por padrão o split() separa os elementos pelos espaços, também posso passar como padrão de separação outros elementos.

--> Para juntar os elementos passando um padrão

* Utilizamos o método join()

nome = ["Marcone", "de", "Freitas", "Marques"]
nome = " ".join(nome)
print(nome)

Como podemos perceber acima, a lista nome que era composta por strings foi juntada, no método join utilizamos o padrão do espaço para ser unido,
e também passamos no parâmetro do método quem devera sofrer a operação.


--> Iterando sobre listas

Podemos utilizar o laço de repetição "for"

nomes = ["Marcone", "Vera", "Letícia", "Ana", "Davi"]

for elemento in nomes:
    print(elemento)


Assim como podemos utilizar o laço de repetição "for", também podemos utilizar o laço de repetição "while".


--> Podemos acessar os elementos de forma indexada

posicoes = [0,1,2,9,4,5,6]

print(posicoes[2]) == 2
print(posicoes[3]) == 9

Podemos também fazer acesso ao índice do elemento além do seu valor

Para isso utilizamos o enumerate(), já mencionado anteriormente.

for indice, valor in enumerate(nome):
    print(indice, valor)


OBS: Listas aceitam valores repetidos


--> Para procurar um elemento pelo índice

Para realizar essa operação utilizamos o método index()

- O indice informado deve ser válido
- Retorna o índice do primeiro a ser encontrado

index(elemento, índice de inicio de busca)

Também podemos passar o ínicio e o fim da pesquisa

numero.index(elemento, inicio, fim)

Podemos também passar como parâmetro de início no range para o index.

numeros = [5,1,3,8,4]

print(numeros.index(5,0))


--> Inverter uma lista

Utilizamos o método reverse()

numeros = [5,1,3,8,4]

print(numeros)

numeros.reverse()

print(numeros)


--> Operações SOMA, VALOR MÁXIMO, VALOR MÍNIMO, TAMANHO

num = [1,2,3,4,5,66]

print(sum(num))
print(max(num))
print(min(num))
print(len(num))


--> Transformar uma lista em uma tupla

numeros = [1,2,4,5,6]

print(numeros)

tupla = tuple(numeros)

print(tupla)


--> Desempacotar uma lista

lista = [1,2,4]

n1, n2, n3 = lista

print(n1,n2,n3)

obs: O número de variáveis deve ser igual ao número de elementos a ser desempacotado da lista


--> Copia de lista

    --> Deep Copy 

lista = [1,2,3]
nova = lista.copy()
nova.append(4)
print(lista)
print(nova)

Utilizando o copy() os dados são copiados para a nova lista, mas ambos são independentes, ou seja, as modificações de uma não afetam a outra.


    --> Shallow Copy

lista = [1,2,3]
nova = lista
nova.append(4)

print(lista)
print(nova)

Neste caso ambos tem ligação direta, assim as modificações em uma também afetam a lista copiada.

"""