#Criação da função
def somaLista(lista):
    #Inicializa uma variável chamada 'soma' com valor zero para armazenar a soma dos números.
    soma = 0

    #Laço para percorrer cada elemento da lista
    for numero in lista:
        #Soma o atual valor do "numero" a variável "soma".
        soma += numero

    #Retorna o valor soma ao fim da iteração.
    return soma

#Lista predefinida:
minhaLista = [7, 17, 27, 37, 47]

#Criação da variável "resultado" que receberá o return da função "somaLista"
resultado = somaLista(minhaLista)

print("A soma dos números na lista é:", resultado)