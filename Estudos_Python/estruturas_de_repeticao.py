"""

Loop "for"


Usamos o laço de repetição "for" quando queremos repetir uma ação um número n de vezes, sendo n um número conhecido.

Alguns exemplos

"""

for i in range(10):
    print(i)

# Vale lembrar que a estrutura acima irá repetir até n-1

for i in range(0,10):
    print(i)

# Novamente vimos que o padrão se repete, uma vez que, o valor passado como delimitação final da estrutura não é inclusivo.

for i in range(1,11,1):
    print(i)

for i in range(1,11,-1):
    print(i)

# Enumerate

nomes = ["Honório", "Flávia", "Carolina", "Pedro"]

for indice, valor in enumerate(nomes):
    print(indice, valor)


"""

Loop while

--> Laço de repetição que se repete n vezes, sendo n um número desconhecido.

Para sair de um laço de repetição while, podemos utilizar o "break", e para continuar para uma próxima interação podemos utilizar o "continue".

Vejamos alguns exemplos abaixo

"""

while True:
    num = int(input())
    if num == 0:
        break

# Como podemos perceber no exemplo acima, quando passarmos para o programa o valor "0" a estrutura do break será acionada e nosso programa seirá do loop que se encontra.

