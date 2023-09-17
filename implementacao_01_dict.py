def somaDiasDoAno(meses):
    #Inicializa uma variável chamada "soma" com valor zero para armazenar a soma dos dias.
    soma = 0

    #Laço para percorrer os elementos do dicionário
    for mes in meses:
        #Soma o valor de cada "mes" a variável soma.
        soma += meses[mes]

    #Retorna o valor "soma".
    return soma

#Criação do dicionário "meses" contendo o nome do mês (chave) e seus respectivos dias (valor).
#Considerar ano não bissexto
diasPorMes = {'Janeiro': 31, 'Fevereiro': 28, 'Marco': 31, 'Abril': 30, 'Maio': 31, 'Junho': 30,
'Julho': 31, 'Agosto': 31, 'Setembro': 30, 'Outubro': 31, 'Novembro': 30, 'Dezembro': 31,
}

resultado = somaDiasDoAno(diasPorMes)
print("O total de dias no ano é:", resultado)