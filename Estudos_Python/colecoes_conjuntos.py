"""

CONJUNTOS

Em Python os conjuntos são mais conhecidos como "sets"

* Não possuem valores duplicados ou ordenados.
* Elementos não são acessados via índice, ou seja, não são indexados.

--> Os conjuntos são usuais para adicionarmos valores dos quais, não nos importamos com sua ordenação, duplicados etc.

Conjuntos x Mapas

conjuntos = Possuem apenas um valor
mapas = possuem chave/valor

--> Definindo conjuntos

S = set({1,2,3,4,5,5,6,7,2,3})
print(S)

Como podemos notar acima os valores 2,3,5 que possuem duplicata aparecem apenas uma vez no conjunto.

--> Consigo converter uma string em um set
--> Consigo converter uma lista em um set
--> Consigo converter uma tupla em um set

--> Assim como as demais coleções em python também podemos adicionar todos os tipos de dados em um conjunto.

--> A iteração ocorre normalmente com 

conjunto = set({1,2,3,4,5,6,7,7,8,7,7,7,7})
print(conjunto)

for elemento in conjunto:
    print(elemento)

--> Nos conjuntos é gerado uma ordenação aleatória, ou seja, não é mantido a ordenação inicial.

--> Adicionar elementos em um conjunto

    - Duplicidade não gera erro, somente não é adicionada a informação.
    - Para adicionar um elemento em um conjunto utilizamos o método .add()

    conjunto = set({1,2,3,4,5,6,7,7,8,7,7,7,7})

    conjunto.add(10)

    print(conjunto)


--> Removendo elementos de um conjunto

    1 - Podemos usar o método remove(valor)

    conjunto.remove(valor)

    conjunto = set({1,2,3,4,5,6,7,7,8,7,7,7,7})

    conjunto.remove(1)

    print(conjunto)

    --> Caso o valor informado não exista teremos como retorno um Keyerror


--> Copiando conjuntos

    1 - Forma Deep Copy

        conjunto = C.copy()

    2 - Forma Shallow Copy

        conjunto = C

--> Remover todos os elementos de um conjunto (Limpar o conjunto)

C = set({1,2,3,45,6,77,6})

print(C)

C = C.clear()

print(C)


--> Gerar conjuntos com elementos únicos

    - Forma 1 (Utilizando o método .union(parãmetro))

        a = set({1,2,3})
        b = set({4,5,6})

        c = a.union(b)

        print(c)
    
    - Forma 2 (Utilizando o caractere "|" pipe)

        a = set({1,2,3})
        b = set({4,5,6})

        c = a|b

        print(c)

--> Gerar conjuntos que estão em ambos os conjuntos (Intersecção de conjuntos)

    - Forma 1 (Utilizando o método intersection())

        a = set({1,5,6})
        b = set({4,5,6})

        print(a.intersection(b))

    - Forma 2 (Utilizando o e-comercial)

        print(a&b)

--> Conjunto com elementos que não estão no outro conjunto 

    - Utilizamos o .difference()

    a = set({1,5,6})
    b = set({4,5,6})

    print(a.difference(b))
    print(b.difference(a))

--> Soma, Valor Máximo, Valor Mínimo e Tamanho

    sum(), max(), min(), len()

    b = set({4,5,6})

    print(sum(b))
    print(max(b))
    print(min(b))
    print(len(b))


Métodos em Conjuntos (Resumo)

* in
* remove()
* copy()
* clear()
* union()
* difference()
* intersection()
* sum()
* max()
* min()
* len()

"""

