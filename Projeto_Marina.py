
"""
Projeto Marina Vilamoura
"""
from datetime import datetime

def validate_date(d):
    try:
        if len(d) == 10:
            datetime.strptime(d, '%d/%m/%Y')
            return True
        else: return False
    except ValueError:
        return False


# LER DOCUMENTO TXT
# Abrir um arquivo de texto para leitura:
ficheiroDadosMarina = "DadosMarina2.txt"
maxLugaresCais = {'caisA': 40, 'caisB': 32, 'caisC': 35, 'caisD': 30, 'caisE': 25, 'caisF': 17, 'caisG': 7}
preco_por_cais = {'caisA': 10.40, 'caisB': 15.50, 'caisC': 19.50,
    'caisD': 25.60, 'caisE': 50.50, 'caisF': 62.80, 'caisG': 80.00}
# esta variavel max = numero total de lugares que temos em cada cais
tipoCais = {
    (0, 7.99): 'caisA',
    (8, 9.99): 'caisB',
    (10, 11.99): 'caisC',
    (12, 14.99): 'caisD',
    (15, 17.99): 'caisE',
    (18, 19.99): 'caisF',
    (20, float('inf')): 'caisG'
}


def read_file(ficheiroDadosMarina):
    fil = open(ficheiroDadosMarina)
    lines = fil.readlines()
    fil.close()
    return lines


def gerirCais(ficheiroDadosMarina):
    lugaresCais = {'caisA': 0, 'caisB': 0, 'caisC': 0, 'caisD': 0, 'caisE': 0, 'caisF': 0, 'caisG': 0}
    # criar um dicionario para guardar o nr de lugares ocupados
    for i in range(len(ficheiroDadosMarina)):  # saber o nr de linhas
        # Vais dividir os | em colunas e divide em lista
        linha = ficheiroDadosMarina[i].split('|')
        # vai buscar o comprimento a coluna 5 do txt
        comprimentoBarco = float(linha[5])
        # a lista e string e nos precisamos de numeros tipo 9.99 logo float

        if comprimentoBarco < 7.99:
            lugaresCais['caisA'] += 1  # adicionar 1 barco ao cais A

        elif 8 <= comprimentoBarco < 9.99:
            lugaresCais['caisB'] += 1

        elif 10 <= comprimentoBarco < 11.99:
            lugaresCais['caisC'] += 1

        elif 12 <= comprimentoBarco < 14.99:
            lugaresCais['caisD'] += 1

        elif 15 <= comprimentoBarco < 17.99:
            lugaresCais['caisE'] += 1

        elif 18 <= comprimentoBarco < 19.99:
            lugaresCais['caisF'] += 1

        elif comprimentoBarco:
            lugaresCais['caisG'] += 1

    return lugaresCais


def getTipoCais(comprimento_do_barco):  # Dar o tipo de cais consoante o comp do barco

    for intervalo, tipo in tipoCais.items():

        if intervalo[0] < comprimento_do_barco < intervalo[1]:
            return tipo
    return None

def listarEmbarcacoes(ficheiroDadosMarina):

    listaEmbarcacoes = {}

    for embarcacao in ficheiroDadosMarina:  # percorre todas as embarcacoes
        # obter o comprimento da 5 posicao
        comprimento = float(embarcacao.split('|')[5])
        # converter o comprimento em tipo de cais
        tipoCais = getTipoCais(comprimento)
        #print(tipoCais)

        if tipoCais not in listaEmbarcacoes:  # se o tipo cais não tiver na listaembarcacoes entao temos uma lista vazia
            listaEmbarcacoes[tipoCais] = []

        # agrupar a lista de embarcacoes nos respetivos cais
        listaEmbarcacoes[tipoCais].append(embarcacao)

    listaEmbarcacoesOrdenada = sorted(
        listaEmbarcacoes.keys())  # ordenar os cais
    #print(listaEmbarcacoesOrdenada)

    for tipo in listaEmbarcacoesOrdenada:  # percorre os cais que ordenamos em cima
        # obtem as embarcacoes e todas as informações ordenadas por cais
        tipoEmbarcacoes = listaEmbarcacoes[tipo]
        print(tipo, tipoEmbarcacoes)

def listar_embarcacoes_por_cais(cais_id, ficheiro):
    if cais_id == 'A':
        cais_id = 'caisA'
    elif cais_id == 'B':
        cais_id = 'caisB'
    elif cais_id == 'C':
        cais_id = 'caisC'
    elif cais_id == 'D':
        cais_id = 'caisD'
    elif cais_id == 'E':
        cais_id = 'caisE'
    elif cais_id == 'F':
        cais_id = 'caisF'
    elif cais_id == 'G':
        cais_id = 'caisG'
    else:
        print('O cais escolhido não existe.')

    listaEmbarcacoes = {}

    for embarcacao in ficheiro:  # percorre todas as embarcacoes
        # obter o comprimento da 5 posicao
        comprimento = float(embarcacao.split('|')[5])
        # converter o comprimento em tipo de cais
        tipoCais = getTipoCais(comprimento)
        #print(tipoCais)

        if tipoCais not in listaEmbarcacoes:  # se o tipo cais não tiver na listaembarcacoes entao temos uma lista vazia
            listaEmbarcacoes[tipoCais] = []

        # agrupar a lista de embarcacoes nos respetivos cais
        listaEmbarcacoes[tipoCais].append(embarcacao)

    listaEmbarcacoesOrdenada = sorted(
        listaEmbarcacoes.keys())  # ordenar os cais
    #print(listaEmbarcacoesOrdenada)

    for tipo in listaEmbarcacoesOrdenada:  # percorre os cais que ordenamos em cima
        # obtem as embarcacoes e todas as informações ordenadas por cais
        if tipo == cais_id: # fazer a logica apenas para o tipo de cais que foi escolhido
            tipoEmbarcacoes = listaEmbarcacoes[tipo]
            print(tipo, tipoEmbarcacoes)

def calcular_valor_a_pagar(matricula_input, ficheiro):
    for embarcacao in ficheiro:

        matricula_do_barco_i = str(embarcacao.split('|')[2])
        if matricula_input == matricula_do_barco_i :

            # get cais_id através do comprimento
            comprimento = float(embarcacao.split('|')[5])
            # converter o comprimento em tipo de cais
            cais_matricula_input = getTipoCais(comprimento)
            # print(cais_matricula_input) 

            preco_por_dia_para_a_matricula = preco_por_cais[cais_matricula_input]

            date_format = "%d/%m/%Y"
            data_entrada = str(embarcacao.split('|')[6])
            data_saida = str(embarcacao.split('|')[7])
            entrada = datetime.strptime(data_entrada, date_format).date()
            saida = datetime.strptime(data_saida, date_format).date()
            diferenca_datas = saida - entrada
            diferenca_em_dias = diferenca_datas.days
            # caso seja para fazer em duas alineas diferentes é só descomentar este bloco
            # valor_total = preco_por_dia_para_a_matricula * diferenca_em_dias
            # print(f'O valor a pagar pelos {diferenca_em_dias} dias é {valor_total} €.')

            if diferenca_em_dias < 10:
                valor_total = preco_por_dia_para_a_matricula * diferenca_em_dias
                print(f'O valor a pagar pelos {diferenca_em_dias} dias é {valor_total} €.')
            else:
                valor_total = preco_por_dia_para_a_matricula * diferenca_em_dias * 0.90
                print(f'Como o tempo de estadia é superior a 10 dias, foi aplicado um desconto de 10%. Assim, o valor a pagar pelos {diferenca_em_dias} dias é {valor_total} €.')

# Escolher a opcao que pretendem realizar:

def apresentarMenu():
    dadosMarina = read_file(ficheiroDadosMarina)
    lugaresCais = gerirCais(dadosMarina)
    
    opcao = 0
    while opcao !=10:   
        print ('''\n\nEscolha a opcão que pretende realizar:
        [1] Nova Embarcação
        [2] Lista de informações de todas as embarcações 
        [3] Informação das embarcações por cais
        [4] Valor a pagar
        [5] Valores pagos até ao momento
        [6] Número de lugares vagos em cada cais
        [7] Prolongamento da estadia
        [8] Informações sobre embarcação com saída prevista
        [9] Obtenha um desconto
        [10] Aumento de tarifas  ''')
        print ('--'*30)
        opcao = int(input('Qual a sua opção: '))
        
        
        if opcao == 1:
            print('Escreva os dados da sua embarcação:')
            nomeProprietario = str(input('Insira o nome do proprietário: '))
            nomeCapitao = str(input('Insira o nome do capitão: '))
            matricula = str(input('Insira a sua matricula: '))
            paisOrigem = str(input('Insira o seu pais de origem: '))
            nrPassageiro = int(input('Insira o numero de passageiros: '))
            dataEntrada = input('Insira a data de entrada (dd/mm/yyyy): ')
            while validate_date(dataEntrada) != True:
                dataEntrada = input('Formato errado. Por favor utilize o formato dd/mm/yyyy: ')
            dataSaida = input('Insira a data de saida (dd/mm/yyyy): ')
            while validate_date(dataSaida) != True:
                dataSaida = input('Formato errado. Por favor utilize o formato dd/mm/yyyy: ')
            comprimentoBarco = float(input('Insira o comprimento fora a fora do barco: '))
            cais = getTipoCais(comprimentoBarco)
            print(cais)
        
           
            if cais != None:
                lugarDisponivel = maxLugaresCais[cais] -  lugaresCais[cais]
                print(lugarDisponivel)
                
                # Esta condição serve para o programa so adicionar novas embarcações qd tiver lugar, caso nao tenha, não adiciona.
                if lugarDisponivel > 0: 
                    novaEmbarcacao = (f'\n{nomeProprietario}|{nomeCapitao}|{matricula}|{paisOrigem}|{nrPassageiro}|{comprimentoBarco}|{dataEntrada}|{dataSaida}|\n')
                    with open ('dadosMarina2.txt','a') as file: # criar a variavel file a= append, ou seja serve para juntar a nova embarcacao a nossa base de dados
                        file.write(novaEmbarcacao)
                        
                    print(f'O barco pertence ao {cais} e este cais tem {lugarDisponivel} lugares disponiveis')        
                else:
                    print(f'Não existem lugares disponíveis para o {cais}')
                 


        if opcao == 2:
            
            listarEmbarcacoes(dadosMarina)

        if opcao == 3:
            caisescolhido = str((input('Escolha um cais de A a G:'))).upper()
            listar_embarcacoes_por_cais(caisescolhido, dadosMarina)

        if opcao == 4:
            matricula_input = str(input('Insira a sua matrícula: '))
            calcular_valor_a_pagar(matricula_input, dadosMarina)

        if opcao == 5:
            pass

        if opcao == 6:
            lugares_livres_por_cais(dadosMarina)

def lugares_livres_por_cais(ficheiro):
    lugares_ocupados = gerirCais(ficheiro)
    lugares_disponiveis = {}
    for cais in maxLugaresCais:
        lugares_disponiveis[cais] = maxLugaresCais[cais] - lugares_ocupados[cais]

    for cais, lugares in lugares_disponiveis.items():
        print(f'{cais} tem {lugares} lugares disponiveis')   


apresentarMenu()
