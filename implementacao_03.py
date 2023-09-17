#Criação da função de pesquisaBinária
def pesquisaBinaria(lista, chave):

    #Criação de duas variáveis para percorrer os elemento na lista que será realizada a pesquisa binária
    #"esquerda" é inicializada em 0, que é a primeira posição da lista, "direita" é inicializada com o valor
    #do tamanho da lista - 1 para indicar o ultimo valor da lista
    esquerda, direita = 0, len(lista) - 1

    #Loop enquanto "esquerda" for menor ou igual a "direita"
    while esquerda <= direita:

        #Criação da variável "meio" e atribuíndo a ela o valor da divisão inteira da soma "esquerda + direita" por 2
        meio = (esquerda + direita) // 2

        #A variável "elementoMeio" recebe o INDICE que corresponde ao valor do "meio" obtido anteriormente
        elementoMeio = lista[meio]

        #Condição que compara se o "elementoMeio" é idêntico ao valor da chave buscada
        if elementoMeio[0] == chave:
            #Se a condição anterior for verdadeira retorna a chave
            return elementoMeio[1:]
        
        #Se a "chave" for menor que o "elementoMeio" significa que a chave está a esquerda indice central da lista ordenada    
        elif chave < elementoMeio[0]:
            #Caso a condição acima seja verdadeira a variável "direita" recebe "meio-1" o que reduz o campo de procura
            #para a metade esquerda da lista
            direita = meio - 1

        #Caso nenhuma condição anterior seja atendida então ocorre o inverso da condição anterior
        else:
            esquerda = meio + 1

    #Caso a chave não seja encontrada
    return "Objeto não encontrado."

def pesquisaArquivo(arquivo, chave):
    try:
        #Utilização do with para que ao fim da execução do bloco o arquivo seja fechado automáticamente
        #Open é utilizado para abrir o arquivo, não é necessário ter o mesmo nome do arquivo pois o nome
        #"correto" deve ser passado nos argumentos ao chamar a função
        #'r' indica o que o arquivo sera apenas lido (read)
        #"file" receberá o conteúdo do arquivo que será lido
        with open(arquivo, 'r') as file:
            #Criação de uma lista vazia
            dados= []
            #Utilização de loop para percorrer as linhas da variável "file" que possui os valores do arquivo "dados.txt"
            for linha in file:
                #A lista "partes" recebe os valores da primeira linha de "file", que com o uso do "strip()" faz a eliminação
                #de espaços em branco no começo e fim da string; "split()" é responsável por separar os valores da primeira
                #linha, por padrão ele separa os valores sempre que identifica um espaço em branco"
                partes = linha.strip().split()
                
                #Como a lista "partes" recebeu os valores separados, agora o valor na primeira posição [0] é a nossa chave
                #"chaveObjeto" recebe o primeiro valor da lista "partes"
                chaveObjeto = partes[0]

                #Adição dos valores da primeira linha em uma tupla em duas partes, uma consiste no primeiro valor da linha
                #partes[0] que é CHAVE e em seguida são adicionados os valores restantes a partir do segundo valor da linha
                #até o ultimo "partes[1: ]", sendo separados por espaços em branco ' ' em uma única string com o uso do .join()
                dados.append((chaveObjeto, ' '.join(partes[1: ])))

            #Com a lista "dados[]" pronta ela será ordenada com base no primeiro elemento de cada tupla dentro dela
            #sort é um método de ordenação com base em um critério especificado, nesse caso a função lambda obtém o primeiro
            #elemento de cada tupla da lista "dados", que são as chaves
            dados.sort(key=lambda x: x[0])

            #Variável "resultado" recebe o resultado da função "pesquisaBinária"
            resultado = pesquisaBinaria(dados, chave)

            return resultado
        
    #Caso o arquivo não seja encontrado será "ativado" a exceção "FileNotFoundError" que é quando o arquivo não
    #é encontrado, retornando assim uma mensagem
    except FileNotFoundError:
        return "Arquivo não encontrado."

#Criação da variável "arquivoDados" que recebe o arquivo a ser lido
arquivoDados = "dados.txt"

#Criação da variável "chaveBuscada" que recebe o valor da chave procurada
chaveBuscada = "115"

#Criação davariável "resultado" para receber o return da função "pesquisaArquivo"
resultado = pesquisaArquivo(arquivoDados, chaveBuscada)
#Para remover a vírgula ao fim da string
resultado = resultado[0].rstrip(',')

#Imprimir mensagem
print(resultado)