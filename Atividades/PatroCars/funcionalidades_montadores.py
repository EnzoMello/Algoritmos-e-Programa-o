from ulid import ULID
from funcionalidades_modelos import adicionar_modelo,lista_modelos,remover_modelos,editar_modelos
from funcionalidades_veiculos import adicionar_veiculo, editar_remover, vende_veiculo,lista_veiculos

# USANDO A VARIÁVEIS GLOBAIS SEM NADA PARA IR MOLDANDO ELAS NO CODIGO. COMO NÃO TEM VALOR, O PADRÃO DELA VAI SE AJUSTANDO
registro_referencia = []
registro_modelos = []
registro_veiculos = []

# CRIANDO MEU MENU PARA O PATROCARS
def menu_geral():
    menu = '''\033[0;34m============= BEM-VINDO AO PATROCARS =============
\033[0;34m-> Por favor,selecione uma opção para encarminhamos você
\033[0;34m[1] -> Montadoras
\033[0;34m[2] -> Modelos de veículos
\033[0;34m[3] -> Veículos
\033[0;34m[4] -> Salvar e Sair
\033[0;34m[5] -> Carregar dados

(0) -> SAIR

\033[0;34m============================================='''
    return menu


# FUNÇÃO PARA SALVAR E SAIR
def salva_sai(registro_referencia, registro_modelos, arquivo, arquivo2):

    with open(arquivo, 'w') as arquivo, open(arquivo2, 'w') as arquivo2:
        for indice1, indice2 in zip(registro_referencia, registro_modelos):
            arquivo.write("{}\n".format(indice1))
            arquivo2.write("{}\n".format(indice2))

# FUNÇÃO PARA CARREGAR DADOS
def carrega_dados():
    global registro_referencia, registro_modelos
    arq1 = input("Nome do arquivo: ")
    arq2 = input("Nome do arquivo: ")


    with open(arq1, 'r') as arquivo:
        for linha in arquivo:
            registro_referencia.append(linha.strip())

    with open(arq2, 'r') as arquivo2:
        for linha in arquivo2:
            registro_modelos.append(linha.strip())

# FUNÇÃO QUE ENCERRA
def encerrar():
    return str("Volte Sempre!!!")

# FUNÇÃO PARA ESCOLHER NÚMERO
def number_positive():
    digito = int(input("Escolha um número do menu: "))

    while digito < 0 or digito > 5:
        print("Número inválido.")
        digito = int(input("Digite um número do menu: "))

    return digito

# FUNÇÃO QUE ENCAMINHA MEU USUÁRIO PARA CADA CRUD
def encaminha_crud(escolha_feita):
    dicionario = {
        '1' : menu_montadoras,
        '2' : menu_modelos,
        '3' : menu_veiculos,
        '4' : salva_sai,
        '5' : carrega_dados,
        '0' : encerrar
       
    }

    crud_escolhido = dicionario[escolha_feita]

    if crud_escolhido == dicionario['4']:
        global registro_referencia, registro_modelos
        return crud_escolhido(registro_referencia,registro_modelos, 'arquivo_montadora.txt', 'arquivo_modelos.txt')
    else:
        return crud_escolhido()

# FUNÇÃO QUE ENCAMINHA PARA O MENU DE MONTADORAS
def menu_montadoras():
    while True:
        print('''\033[0;35m----------> SEÇÃO "CRUD" MONTADORAS <-----------
    \033[0;035m-> Por favor,selecione uma opção para ajudá-lo:
    \033[0;035m[1] -> Listar montadoras
    \033[0;035m[2] -> Cadastrar montadoras
    \033[0;035m[3] -> Modificar montadoras
    \033[0;035m[4] -> Excluir montadoras
    \033[0;035m[5] -> Filtrar montadoras

    (0) -> SAIR DESSA SEÇÃO 
    \033[0;35m----------------------------------------------------''')

        escolher = number_positive()
        if escolher == 0:
            break
        else:
            return opcao_montadora(str(escolher))
        
# FUNÇÃO QUE ENCAMINHA DENTRO DO CRUD MONTADORAS
def opcao_montadora(escolha_feita):
    global registro_referencia

    if escolha_feita == '2':
        montando = dados_montadora(escolha_feita)
        registro_referencia += montando
    if escolha_feita == '1':
        lista_montadora(registro_referencia)
    elif escolha_feita == '3':
        modificar_montadora(registro_referencia)
    elif escolha_feita == '4':
        excluir_montadora(registro_referencia)
    elif escolha_feita == '5':
        filtrar_montadora(registro_referencia)


# FUNÇÃO PARA INCREMENTAR DADOS
def dados_montadora(escolha_feita):
    registro_geral = []

    if str(escolha_feita) == '2':
        gerar_id = int(ULID())
        nome = input("\033[0;33mNome da montadora: ")
        pais = input("\033[0;33mPaís de origem: ")
        ano = int(input("\033[0;33mAno de fundação: "))

        registro_geral.append({"id" : gerar_id, "nome" : nome, "pais" : pais, "ano_fundacao" : ano})
        
    return registro_geral

# FUNÇÃO QUE LISTA OS DADOS DO MEU VETOR
def lista_montadora(registro_geral):
    
    ordenar = input("Ordenar a lista antes de exibir?(SIM/NAO): ").upper()
    if ordenar == 'SIM':
            print('''[0;33m********* ESCOLHA DO ATRIBUTO *********
    [0;33m[1] -> Nome
    [0;33m[2] -> País
    [0;33m[3] -> Ano de Fundação
    [0;33m************************************''')
            atributo = int(input("[0;33mEscolha uma opção: "))
            tamanho = input("[0;33mForma de ordenação(ASC/DESC): ").upper()
            
            # LISTA POR NOMES
            if atributo == 1:
                nomes = []
                for registro in registro_geral:
                    nomes.append(registro["nome"])

                # USANDO O ALGORITMO BUBBLE SORT PARA ORDENAR EM QUESITO TAMANHO
                    if tamanho == 'ASC':
                        for i in range(len(nomes)):
                            for j in range(0,len(nomes) - i - 1):
                                if nomes[j] > nomes[j + 1]:
                                    nomes[j], nomes[j + 1] = nomes[j + 1],nomes[j]
                    else:
                        for i in range(len(nomes)):
                            for j in range(0,len(nomes) - i - 1):
                                if nomes[j] < nomes[j + 1]:
                                    nomes[j], nomes[j + 1] = nomes[j + 1],nomes[j]

                print(nomes)

            #LISTA POR PAÍSES
            elif atributo == 2:
                paises = []
                for registro in registro_geral:
                    paises.append(registro["pais"])

                # USANDO O BUBBLE SORT PARA ORDENAR EM TAMANHO
                    if tamanho == 'ASC':
                        for i in range(len(paises)):
                            for j in range(0,len(paises) - i - 1):
                                if paises[j] > paises[j + 1]:
                                    paises[j], paises[j + 1] = paises[j + 1],paises[j]
                    else:
                        for i in range(len(paises)):
                            for j in range(0,len(nomes) - i - 1):
                                if paises[j] < paises[j + 1]:
                                    paises[j], paises[j + 1] = paises[j + 1],paises[j]


                print(paises)
            
            #LISTA POR ANOS
            elif atributo == 3:
                anos = []
                for registro in registro_geral:
                    anos.append(registro["ano_fundacao"])

                    # USANDO O BUBBLE SORT PARA ORDENAR EM TAMANHO
                    if tamanho == 'ASC':
                        for i in range(len(anos)):
                            for j in range(0,len(anos) - i - 1):
                                if anos[j] > anos[j + 1]:
                                    anos[j], anos[j + 1] = anos[j + 1],anos[j]
                    else:
                        for i in range(len(anos)):
                            for j in range(0,len(anos) - i - 1):
                                if anos[j] < anos[j + 1]:
                                    anos[j], anos[j + 1] = anos[j + 1],anos[j]

                print(anos)
            else:
                print("Lista vazia")
    else:
        print(registro_geral)

# FUNÇÃO QUE MODIFICA UMA MONTADORA DO MEU VETOR
def modificar_montadora(registro_geral):
    print(registro_geral)

    escolha = int(input("\033[0;33mA primeira montadora é a número 0, selecione qual deseja alterar: "))
    registro_geral.pop(escolha)
    gerar_id = int(ULID())
    nome = input("\033[0;33mNome da montadora: ")
    pais = input("\033[0;33mPaís de origem: ")
    ano = int(input("\033[0;33mAno de fundação: "))

    # MÉTODO INSERT INSERE UM ELEMENTO EM UMA POSIÇÃO ESPECÍFICA.NESSE CASO, A NOSSA POSIÇÃO JÁ VEM LIVRE, POIS FOI EXCLUÍDA ANTES
    registro_geral.insert(escolha,{"id" : gerar_id, "nome" : nome, "pais" : pais, "ano_fundacao" : ano})
    return registro_geral

# FUNÇÃO QUE EXCLUI MONTADORA
def excluir_montadora(registro_geral):
    print(registro_geral)

    escolha = int(input("\033[0;33mA primeira montadora é a número 0, selecione qual deseja excluir: "))
    registro_geral.pop(escolha)

    return registro_geral

# FUNÇÃO QUE FILTRA MONTADORA
def filtrar_montadora(registro_geral):
    encontrar = input("\033[0;33mDigite o que você busca encontrar: ")
    ordenar = input("\033[0;33mOrdenar a lista antes de exibir?(SIM/NAO): ").upper()

    if ordenar == 'SIM':
        print('''\033[0;33m********* ESCOLHA DO ATRIBUTO *********
    \033[0;33m[1] -> Nome
    \033[0;33m[2] -> País
    \033[0;33m[3] -> Ano de Fundação
    \033[0;33m************************************''')
        atributo = int(input("Escolha uma opção: "))
        tamanho = input("Forma de ordenação(ASC/DESC): ").upper()

        
        if atributo == 1:
                nomes = []
                for registro in registro_geral:
                    nomes.append(registro["nome"])

                # USANDO O ALGORITMO BUBBLE SORT PARA ORDENAR EM QUESITO TAMANHO
                    if tamanho == 'ASC':
                        for i in range(len(nomes)):
                            for j in range(0,len(nomes) - i - 1):
                                if nomes[j] > nomes[j + 1]:
                                    nomes[j], nomes[j + 1] = nomes[j + 1],nomes[j]
                    else:
                        for i in range(len(nomes)):
                            for j in range(0,len(nomes) - i - 1):
                                if nomes[j] < nomes[j + 1]:
                                    nomes[j], nomes[j + 1] = nomes[j + 1],nomes[j]                        
                    
                print(nomes)
                if encontrar in nomes:
                    print("Palavra encontrada: {}".format(encontrar))
                else:
                    print("Palavra não encontrada.")
        elif atributo == 2:
            paises = []
            for registro in registro_geral:
                paises.append(registro["pais"])

                # USANDO O BUBBLE SORT PARA ORDENAR EM TAMANHO
                if tamanho == 'ASC':
                    for i in range(len(paises)):
                        for j in range(0,len(paises) - i - 1):
                            if paises[j] > paises[j + 1]:
                                paises[j], paises[j + 1] = paises[j + 1],paises[j]
                else:
                    for i in range(len(paises)):
                        for j in range(0,len(nomes) - i - 1):
                            if paises[j] < paises[j + 1]:
                                paises[j], paises[j + 1] = paises[j + 1],paises[j]


            print(paises)
            if encontrar in nomes:
                print("País encontrado: {}".format(encontrar))
            else:
                print("País não encontrado.")
        else:
                anos = []
                for registro in registro_geral:
                    anos.append(registro["ano_fundacao"])

                    # USANDO O BUBBLE SORT PARA ORDENAR EM TAMANHO
                    if tamanho == 'ASC':
                        for i in range(len(anos)):
                            for j in range(0,len(anos) - i - 1):
                                if anos[j] > anos[j + 1]:
                                    anos[j], anos[j + 1] = anos[j + 1],anos[j]
                    else:
                        for i in range(len(anos)):
                            for j in range(0,len(anos) - i - 1):
                                if anos[j] < anos[j + 1]:
                                    anos[j], anos[j + 1] = anos[j + 1],anos[j]

                print(anos)
                if int(encontrar) in anos:
                    print("Ano encontrado: {}".format(encontrar))
                else:
                    print("Ano não encontrado.")
    else:
        if encontrar in registro_geral or int(encontrar) in registro_geral:
            print("Termo está cadastrado: {}".format(encontrar))
        else:
            print("Termo não está cadastrado.")


## CRUD MODELOS DE VEICULOS
# CRIANDO O MENU DE MODELOS DE VEÍCULOS
def menu_modelos():
    print('''\033[0;36m----------> SEÇÃO "CRUD" MODELOS <-----------
    \033[0;36m-> Por favor,selecione uma opção para ajudá-lo:
    \033[0;36m[1] -> Adicionar Modelos de veículos
    \033[0;36m[2] -> Listar Modelos de veículos
    \033[0;36m[3] -> Modificar Modelos de veículos
    \033[0;36m[4] -> Excluir Modelos de veículos
    \033[0;36m[5] -> Filtrar Modelos de veículos

    (0) -> SAIR DESSA SEÇÃO 
\033[0;36m----------------------------------------------------''')

    escolher = number_positive()
    return opcao_modelos(str(escolher))

# FUNÇÃO QUE ENCAMINHA DENTRO DO CRUD MODELOS
def opcao_modelos(escolha_feita):
    global registro_referencia, registro_modelos

    if escolha_feita == '1':
        modelos_veiculos = adicionar_modelo(registro_referencia)
        registro_modelos += modelos_veiculos
    elif escolha_feita == '2':
        listando = lista_modelos(registro_modelos)
        print(listando)
    elif escolha_feita == '3':
        remover_modelos(registro_modelos)
    elif escolha_feita == '4':
        editar_modelos(registro_modelos)

## CRUD VEICULOS
# CRIANDO O MENU DE VEÍCULOS
def menu_veiculos():
    print('''\033[0;32m----------> SEÇÃO "CRUD" VEÍCULOS <-----------
    \033[0;32m-> Por favor,selecione uma opção para ajudá-lo:
    \033[0;32m[1] -> Adicionar veículos
    \033[0;32m[2] -> Editar/Remover veículos
    \033[0;32m[3] -> Vender veículos
    \033[0;32m[4] -> Listar veículos
    (0) -> SAIR DESSA SEÇÃO
\033[0;32m---------------------------------------------------- ''')

    escolher = number_positive()
    return opcao_veiculos(str(escolher))

def opcao_veiculos(escolha_feita):
    global registro_modelos, registro_veiculos

    if escolha_feita == '1':
        veiculos = adicionar_veiculo(registro_modelos)
        registro_veiculos += veiculos
    elif escolha_feita == '2':
        editar_remover(registro_veiculos)
        print("Removido/editado com de acordo com sua preferência.")
    elif escolha_feita == '3':
        vende_veiculo(registro_veiculos)
    elif escolha_feita == '4':
        listando = lista_veiculos(registro_veiculos)
        print(listando)

