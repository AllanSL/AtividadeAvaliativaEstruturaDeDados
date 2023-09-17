def somaLista(lista):
    #Caso base: se a lista estiver vazia, a soma é 0.
    if not lista:
        return 0
    else:
        #Retorna a soma do primeiro elemento + a soma dos restantes, vindo da recursividade
        return lista[0] + somaLista(lista[1:])

#Lista predefinida de nmeros
listaNumeros = [7, 4, 9, 2, 8]

#Criação da variável "resultado" para receber o return da função "somaLista"
resultado = somaLista(listaNumeros)

#Imprimir resultado
print("A soma dos elementos da lista é:", resultado)