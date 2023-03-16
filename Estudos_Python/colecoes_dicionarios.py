"""

DICIONÁRIOS

Em outras linguagens de programação são conhecidos como mapas

    - São um tipo de coleções que possuem chave/valor
    - Nas listas e tuplas as chaves ficam implicitas

Dicionários são representados por chaves {}

--> Declaração de dicionários

    - Forma 1 (Forma mais usual)

    paises = {"br": "Brasil", "eua": "Estados Unidos"}
    2 itens = 2 chaves e 2 valores


 - Chave e valor são separados por ":"
 - Tanto chave quanto valor podem ser de qualquer tipo de dados.

    - Forma 2 

        paises = dict(br = "Brasil", eua = "Estados Unidos")

    
--> Acessando elementos em um dicionário

    - Forma 1 (Via Chave)

    ex : print(paises["br"])

    Caso a chave que estou tentando acessar não exista tenho como retorno um KeyError


    - Forma 2 (Via get)

    Os dicionários possuem um método específico para busca de valores, o get(), 
    no qual podemos passar como parâmetros a chave que queremos e um valor padrão para retornar 
    caso essa chave não seja encontrada:

    print(paises.get(""))

    paises = {"br": "Brasil", "eua": "Estados Unidos"}

    print(paises["br"])

    print(paises.get("br", "País não foi encontrado"))
    print(paises.get("uk", "País não foi encontrado"))

-----------------------------------------------------------------------------------------------------

TIPO NONE

Em python o tipo NONE representa o tipo sem tipo, ou também poderia ser conhecido como tipo vazio.
Sempre a primeira letra maiúscula None
Usado quando queremos criar uma variável inicializado sem um tipo, antes de receber um valor final.


------------------------------------------------------------------------------------------------------

No get quando não encontramos a chave temos como retorno o None
O tipo None em python é sempre considerado "False"

--> Passar o parâmetro caso não exista

Nos dicionários é feita uma busca pela chave e não pelo valor

--> Em dicionários podemos usar qualquer tipos de dados como chave de dicionário, inclusive um outro dicionário, tuplas ou listas.

--> Adicionando elementos em um dicionário

    Forma 1 (Mais comum)

    dicionario["chave"] = valor


    Forma 2 (Menos usual)

    novo_dado = {"chave": 500}
    dicionario.update(novo_dado)


--> Atualizando dados em um dicionário

    Forma 1 (Mais usual)

    dicionario["chave"] = valor


    Forma 2 (Menos usual)

    dicionario.update({"chave": valor})


--> Remover dados de um dicionário

    Forma 1

    dicionario.pop("chave")

    -- Não encontrando a chave passada retorna Keyerror

    Forma 2
    
    del dicionario["chave"]


--> Métodos em dicionários

    --> Para limpar um dicionário

    dicionario.clear()

    --> Para fazer uma cópia do dicionário

        1 - Para fazer uma cópia com copy() - Deep Copy
        2 - Para fazer uma cópia por atribuição - Shallow Copy

--> Outra forma de criar um dicionário (Menos usual)

    outro = {}.fromkeys("chave":"valor")

    - O método fromkeys recebe dois parâmetros um iterável e um valor
    - Ele vai gerar para cada valor de iterável uma chave e irá atribuir a esta chave o valor informado

--> Iterando sobre dicionários

    for chave in dicionario:
        print(chave)

    for chave in dicionario:
        print(dicionario[chave])

--> Para mostrar todas as chaves

    dicionario.keys()

--> Para mostrar todos os valores

    dicionario.values()

--> Desempacotamento de dicionarios

    for chave, valor in dicionario.itens():
        print(f"Chave = {chave} e valor = {valor}")

--> Soma, Valor Máximo, Valor Mínimo

    sum(), max(), min()

--> Tamanho

    len()


paises = {"br": "Brasil", "eua": "Estados Unidos", "uk": "Reino Unido", "cn": "Canadá"}

#Acessando o valor

print(paises["cn"])
print(paises.get("cn", "Não encontrei o país solicitado"))
print(paises.get("jp", "Não encontrei o país solicitado"))


# Adicionando um país no dicionário

paises["jp"] = "Japão"

print(paises)

# Atualizando os dados de um dicionário

paises["eua"] = "Estados Unidos da América"
print(paises)

# Removendo dados de um dicionário

paises.pop("jp")
print(paises)

del paises["eua"]
print(paises)

# Mostrando todas as chaves

print(paises.keys())
print(paises.values())

# Verificando o tamanho do dicionário

print(len(paises))
"""