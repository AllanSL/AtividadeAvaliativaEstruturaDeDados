def maiorTitulo(livros):
    #Inicializa uma variável chamada 'quantidadeLivros' com valor zero para contar os livros.
    quantidadeLivros = 0

    #Inicializa uma variável chamada 'maiorLivro' com uma string vazia.
    maiorLivro = ""

    #Laço para percorrer os livros na tupla "listaLivros"
    for livro in livros:
        #Soma 1 a variável contagem para cada elemento na tupla.
        quantidadeLivros += 1

        #Verifica se o título do livro atual é maior que o título do maior livro encontrado até agora.
        if len(livro) > len(maiorLivro):
            #Caso o resultado anterior seja verdadeiro a variável "maiorLivro" recebe o valor de "livro"
            maiorLivro = livro

    #Retorna uma tupla com o total de livros e o título mais longo.
    return (quantidadeLivros, maiorLivro)

#Criação da tupla "listaLivros" com valores predefinidos
listaLivros = ("As Flores do Mal", "A Divina Comédia", "A Gaia Ciência", "O exército de um homem só")

#Tentativa de alterar o valor na primeira posição da tupla, que retornará erro
#listaLivros[0]= "Dom Quixote"

#Criação da variável resultado que recebe o return da função "maiorTitulo"
resultado = maiorTitulo(listaLivros)

#Imprimir o valor da primeira posição da tupla fornecida pelo return da função "maiorTitulo"
#Que é o valor do total de livros (quantidadeLivros)
print("Total de livros:", resultado[0])

#Imprimir o valor da segunda posição da tupla fornecida pelo return da função "maiorTitulo"
#Que é o valor do maior titulo (maiorLivro)
print("Livro mais longo:", resultado[1])

#Imprimir o tamanho do valor na segunda posição da tupla fornecida pelo return da função "maiorTitulo"
#Utilizando a função built-in "len"
print("Quantidade de caracteres do título do livro mais longo:", len(resultado[1]))
