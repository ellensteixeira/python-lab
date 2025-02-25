# listas são usadas para armazenar um conjunto de itens em uma variável, de forma ordenada.
lista = (1, 2, 'macarrão', 'tomate')
print(lista)

# criando uma lista com números de 1 a 100
numeros = list(range(1, 101))

# a função range() retorna essa sequência de números, incrementando em 1 até o número especificado.
# ela exibe os números de forma ordenada, então ele começa a partir do 0, por isso se coloca 1 número a mais

# usando um laço de repetição for, que significa 'para'
for numero in numeros: # para cada número dentro da lista de números
    if numero % 2 == 0 and numero % 4 == 0: # verifique se o número é par e se é divisível por 4
        print(numero) # se for true (verdadeiro) então exiba os números

# criando agora uma lista usando list comprehension --------------
# o list comprehension serve para encurtar a sintaxe do seu código e gera uma nova lista para você

numbers = list(range(1, 101))

# gera uma nova lista na variável 'par_div'
par_div = [number for number in numbers if number % 2 == 0 and number % 4 == 0]
print(par_div)

# o código funciona na mesma lógica do primeiro código, porém ele é feito em uma única linha
# sua exibição no terminal também é em um formato diferente