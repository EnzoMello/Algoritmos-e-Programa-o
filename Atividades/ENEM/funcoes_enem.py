import csv


# FUNÇÃO DO MEU MENU PRINCIPAL
def menu_principal():
    menu = '''\033[0;035m<------------------------------------------> CONSULTAS ENEM <--------------------------------------------------------------->
\033[0;035m[1] -> TOP N BRASIL (TODAS AS ÁREAS)        | [5] -> MÉDIA NACIONAL POR ÁREA                                |  [9] -> RANKING ENEM POR ESTADO
\033[0;035m[2] -> TOP BRASIL POR ÁREA                  | [6] -> MELHOR ESCOLA POR ÁREA E ESTADO OU BR                  |  [10] -> RANKING ENEM P/REGIÃO PAÍS
\033[0;035m[3] -> TOP BRASIL POR ESTADO                | [7] -> LISTAR ESCOLAS POR ESTADO ORDENADO POR RENDA           |  
\033[0;035m[4] -> TOP BRASIL POR ESTADO E REDE         | [8] -> BUSCA ESCOLA ESPECÍFICA POR PARTE DO NOME              |  [0] = SAIR
\033[0;035m<--------------------------------------------------------------------------------------------------------------------------------------------------->'''

    return menu

# FUNÇÃO PARA OBTER O VALOR DA CHAVE : VALOR ['NOTA']
def obter_valor(dicionario):
    return dicionario['nota']

# FUNÇÃO PARA OPÇÃO 1
def top_brasil():
    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
    
        ranking = []

        # AO LER MEU ARQUIVO, PERCORRO CADA UM E FAÇO A MÉDIA DAS NOTAS
        for linha in arquivo_csv:
            nota = float(linha[12].replace(",","."))
            nome = linha[1]
            ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})

        # COM O SORTED, ORDENO MINHA LISTA DE DICIONÁRIOS POR MEIO DA CHAVE NOTA. O REVERSE AJUDA A FICAR DECRESCENTE
        ranking_ordenado = sorted(ranking, key=obter_valor, reverse=True)

        top = int(input("Informe o limite(EX: 20 = top 20): "))
        return ranking_ordenado[:top]
    
# FUNÇÃO PARA OPÇÃO 2
def top_area():
    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
    
        ranking = []

        escolha = input("Selecione a área(redação,linguagens,humanas,natureza,matemática): ").strip().upper()

        if escolha == "REDAÇÃO":
            for linha in arquivo_csv:
                nota = float(linha[7].replace(",","."))
                nome = linha[1]
                ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
        elif escolha == "LINGUAGENS":
            for linha in arquivo_csv:
                nota = float(linha[8].replace(",","."))
                nome = linha[1]
                ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
        elif escolha == "HUMANAS":
            for linha in arquivo_csv:
                nota = float(linha[9].replace(",","."))
                nome = linha[1]
                ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
        elif escolha == "NATUREZA":
            for linha in arquivo_csv:
                nota = float(linha[10].replace(",","."))
                nome = linha[1]
                ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
        elif escolha == "MATEMÁTICA":
            for linha in arquivo_csv:
                nota = float(linha[11].replace(",","."))
                nome = linha[1]
                ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})  

        ranking.append({'nome' : nome ,'nota' : "{:.2f}\n".format(nota)})

        # COM O SORTED, ORDENO MINHA LISTA DE DICIONÁRIOS POR MEIO DA CHAVE NOTA. O REVERSE AJUDA A FICAR DECRESCENTE
        ranking_ordenado = sorted(ranking, key=obter_valor, reverse=True)

        top = int(input("Informe o limite(EX: 20 = top 20): "))
        return ranking_ordenado[:top]

# FUNÇÃO PARA OPÇÃO 3:
def top_estado():
    estado = input("Digite a sigla representante do estado: ").upper()

    while len(estado) > 2:
        estado = input("Coloque uma sigla válida: ")

    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
    
        ranking = []

        for linha in arquivo_csv:
            if linha[3] == estado:
                nota = float(linha[12].replace(",","."))
                nome = linha[1]
                estado_escola = linha[2]
                ranking.append({'nome' : nome ,'Estado' : estado_escola, 'nota' : "{:.2f}".format(nota)})
            
        top = int(input("Informe o limite(EX: 20 = top 20): "))
        return ranking[:top]
    
# FUNÇÃO PARA OPÇÃO 4:
def top_estado_rede():
    top = int(input("Informe o limite(EX: 20 = top 20): "))
    estado = input("Digite a sigla representante do estado: ").upper()
    rede = input("Qual o tipo de rede de ensino?(Estadual/Privada): ")

    while len(estado) > 2:
        estado = input("Coloque uma sigla válida: ")

    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
    
        ranking = []

        for linha in arquivo_csv:
            if linha[3] == estado and linha[4] == rede:
                nota = float(linha[12].replace(",","."))
                nome = linha[1]
                estado_escola = linha[2]
                rede = linha[4]
                ranking.append({'nome' : nome ,'Rede' : rede,'Estado' : estado_escola, 'nota' : "{:.2f}".format(nota)})
        
        return ranking[:top]

# FUNÇÃO PARA OPÇÃO 5
def media_nacional_area():
    
    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
        escolha = input("Selecione a área(redação,linguagens,humanas,natureza,matemática): ").strip().upper()
        media = 0
        escolas = 0

        for linha in arquivo_csv:
            escolas += 1
            if escolha == 'REDAÇÃO':
                media += float(linha[7].replace(",","."))
            elif escolha == 'LINGUAGENS':
                media += float(linha[8].replace(",","."))
            elif escolha == 'HUMANAS':
                media += float(linha[9].replace(",","."))
            elif escolha == 'NATUREZA':
                media += float(linha[10].replace(",","."))
            elif escolha == 'MATEMÁTICA':
                media += float(linha[11].replace(",","."))
            
        media_nacional = media / escolas
        return "{:.2f} pontos.".format(media_nacional)

# FUNÇÃO PARA OPÇÃO 6
def melhor_escola():
    formato = input("Melhor escola por área e estado ou BR?(E/BR): ").upper()

    if formato == 'E':
        top = int(input("Informe o limite(EX: 20 = top 20): "))
        escolha = input("Selecione a área(redação,linguagens,humanas,natureza,matemática): ").strip().upper()
        estado = input("Digite a sigla representante do estado: ").upper()

        with open("planilha.txt.csv", "r") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=";")
    
            ranking = []

            for linha in arquivo_csv:
                if linha[3] == estado:
                    if escolha == "REDAÇÃO":
                        nota = float(linha[7].replace(",","."))
                        nome = linha[1]
                        ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
                    elif escolha == "LINGUAGENS":
                        nota = float(linha[8].replace(",","."))
                        nome = linha[1]
                        ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
                    elif escolha == "HUMANAS":
                        nota = float(linha[9].replace(",","."))
                        nome = linha[1]
                        ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
                    elif escolha == "NATUREZA":
                        nota = float(linha[10].replace(",","."))
                        nome = linha[1]
                        ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
                    elif escolha == "MATEMÁTICA":
                        nota = float(linha[11].replace(",","."))
                        nome = linha[1]
                        ranking.append({'nome' : nome ,'nota' : "{:.2f}".format(nota)})
            
            return ranking[:top]
    else:
        return top_area()
    
# FUNÇÃO PARA OPÇÃO 7
def lista_ordenada_renda():
    dicionario_parametros = {'ito Alto' : 7,
    'to' : 6,
    'dio Alto' : 5,
    'dio' : 4,
    'dio Baixo' : 3,
    'ixo' : 2,
    'ito Baixo' : 1
    }

    estado = input("Digite a sigla representante do estado: ").upper()
    top = int(input("Informe o limite(EX: 20 = top 20): "))

    with open("planilha.txt.csv", "r") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=";")
    
            ranking = []

            for linha in arquivo_csv:
                if linha[3] == estado:
                    palavra = linha[6][2:].strip()
                    renda = dicionario_parametros['{}'.format(palavra)]
                    nome = linha[1]
                    ranking.append({'nome' : nome ,'Renda(6 até 1)' : renda})
        
            return ranking[:top]
    # ESTILO DOS CARACTERES NA COLUNA DE RENDA ATRAPALHOU A FUNÇÃO

# FUNÇÃO PARA OPÇÃO 8
def busca_escola():
    parte = input("Digite a parte do nome: ").strip()

    with open("planilha.txt.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
    
        ranking = []

        for linha in arquivo_csv:
            nome = linha[1].strip()
            if parte.upper() in nome.upper():
                nota = float(linha[12].replace(",","."))
                ranking.append({'nome' : nome, 'nota' : nota})
        
        return ranking

# FUNÇÃO PARA OBTER_NOTA ESTADO NA OPÇÃO 9
def obter_nota(item):
    return item[1]

# FUNÇÃO PARA OPÇÃO 9
def ranking_estado():
    top = int(input("Informe o limite(EX: 20 = top 20): "))

    with open("planilha.txt.csv", "r") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=";")
            ranking = {}

            for linha in arquivo_csv:
                nota = float(linha[12].replace(",","."))
                if linha[3] in ranking:
                    ranking[linha[3]] += nota
                else:
                    ranking[linha[3]] = nota
                
            #  ORDENO DECRESCENTEMENTE. ITEMS() VAI TRANSFORMAR A LISTA PARA(ESTADO,VALOR),OU SEJA,TUPLAS E A FUNÇÃO OBTER_NOTA PEGA SÓ O VALOR PARA COMPARAR E ORDENAR
            ranking_ordenado = sorted(ranking.items(), key=obter_nota, reverse=True)

            return ranking_ordenado[:top]

# FUNÇÃO PARA OPÇÃO 10
def ranking_regiao():
    regiao = input("Selecione a região(NORTE,NORDESTE,CENTRO-OESTE,SUDESTE,SUL): ").upper()


    with open("planilha.txt.csv", "r") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=";")
            ranking = {}

            norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
            nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
            centro_oeste = ['DF', 'GO', 'MS', 'MT']
            sudeste = ['SP', 'RJ', 'MG', 'ES']
            sul = ['PR', 'SC', 'RS']

            for linha in arquivo_csv:
                if regiao == 'NORTE':
                    if linha[3] in norte:
                        nome_estado = linha[3]
                        nota = float(linha[12].replace(",","."))
                        if nome_estado in ranking:
                            ranking[nome_estado] += nota
                        else:
                            ranking[nome_estado] = nota
                elif regiao == 'NORDESTE':
                        if linha[3] in nordeste:
                            nome_estado = linha[3]
                            nota = float(linha[12].replace(",","."))
                            if nome_estado in ranking:
                                ranking[nome_estado] += nota
                            else:
                                ranking[nome_estado] = nota
                elif regiao == 'CENTRO-OESTE':
                        if linha[3] in centro_oeste:
                            nome_estado = linha[3]
                            nota = float(linha[12].replace(",","."))
                            if nome_estado in ranking:
                                ranking[nome_estado] += nota
                            else:
                                ranking[nome_estado] = nota
                elif regiao == 'SUDESTE':
                        if linha[3] in sudeste:
                            nome_estado = linha[3]
                            nota = float(linha[12].replace(",","."))
                            if nome_estado in ranking:
                                ranking[nome_estado] += nota
                            else:
                                ranking[nome_estado] = nota
                else:
                        if linha[3] in sul:
                            nome_estado = linha[3]
                            nota = float(linha[12].replace(",","."))
                            if nome_estado in ranking:
                                ranking[nome_estado] += nota
                            else:
                                ranking[nome_estado] = nota
                
            #  ORDENO DECRESCENTEMENTE. ITEMS() VAI TRANSFORMAR A LISTA PARA(ESTADO,VALOR),OU SEJA,TUPLAS E A FUNÇÃO OBTER_NOTA PEGA SÓ O VALOR PARA COMPARAR E ORDENAR
            ranking_ordenado = sorted(ranking.items(), key=obter_nota, reverse=True)

            return ranking_ordenado