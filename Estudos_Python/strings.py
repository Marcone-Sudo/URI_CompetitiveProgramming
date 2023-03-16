""" 
Podemos considerar como sendo uma string tudo aquilo que estiver entre

*Aspas simples
*Aspas duplas
*Aspas simples triplas
*Aspas triplas duplas

--> Os principais métodos utiizados em stirngs são:

.lower() --> Transforma todas os elementos para minúsculo
.upper() --> Transforma todos os elementos para maiúsculo
.capitalize() --> Transforma a primeira letra de uma string para maiúscula
.split() --> Remove os espaços tanto a direita quanto a esquerda da string
.strip() --> Quebra a string de acordo com o padrão estabelecido passado por meio de parâmetro, por padrão o separador é o espaço
.len() --> Apresenta o tamanho da cadeia de caracteres que compõe a string

Slicing de strings

        print(string[inicio, fim, passo])


Inverter uma string

        print(string[::-1])

        --> Irei começar no início da string e percorre-la até o último elemento, tomando como passo o -1

"""

nome = "Marcone"
nome_completo = "Marcone de Freitas Marques"


print(nome.lower())
print(nome.upper())
print()
print(nome_completo.capitalize())

fruta = " Melão  "

print(len(fruta))

fruta = fruta.strip()

print(len(fruta))

print(nome_completo.split())

print(nome[::-1])

"""
--> Escopo de variáveis

* Variáveis Globais : São reconhecidas em todo o código, ou seja, seu escopo compreende todo o programa.

* Variáveis Locais : São reconhecidas somente no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco que foi declarado.


obs: Python possuí uma tipagem dinâmica forte, ou seja, não precisamos declarar o tipo de dados ao programar, sendo de responsabilidade da própria linguagem realizar essa atividade.

"""
