import random
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

            #Loop para percorrer o primeiro valor[0] da lista dados, onde encontra-se a chave buscada, então é retornado o
            #restante da lista, excluindo o valor da chave. CHAVE BUSCADA: 111
            for item in dados:
                if item[0] == chave:
                    return item[1:]
            #Mensagem a ser mostrada caso a chave não esteja presente na lista
            return "Chave não encontrada"
        
    #Caso o arquivo não seja encontrado será "ativado" a exceção "FileNotFoundError" que é quando o arquivo não
    #é encontrado, retornando assim uma mensagem
    except FileNotFoundError:
        return "Arquivo não encontrado."

#Criação da variável "arquivoDados" que recebe o arquivo a ser lido
arquivoDados = "dados.txt"

#Criação da variável "chaveBuscada" que recebe o valor da chave procurada gerado aletóriamente com o metodo randint()
chaveBuscada = str(random.randint(100,120))

#Criação davariável "resultado" para receber o return da função "pesquisaArquivo"
resultado = pesquisaArquivo(arquivoDados, chaveBuscada)
#Para remover a vírgula ao fim da string
resultado = resultado[0].rstrip(',')

#Imprimir mensagem
print(resultado)