from ulid import ULID

# FUNÇÃO QUE PERMITE ADICIONAR VEICULO A UM MODELO CADASTRADO
def adicionar_veiculo(registro_veiculos):
    dicionarios_veiculos = []

    # ITERANDO SOBRE A LISTA DE DICIONÁRIOS E USANDO ENUMERATE PARA PEGAR O ÍNDICE DE CADA MODELO JUNTO COM SEU DIC CORRESPONDENTE. ADICIONO A CHAVE MODELO VAZIA NO MEU NOVO DIC 
    for id_modelo, modelo in enumerate(registro_veiculos):
        dicionarios_veiculos.append({"{}".format(modelo["nome_modelo"]): {}})

    print(dicionarios_veiculos)
    escolha = int(input("Começando no 0, escolha o modelo respectivo para incrementar com um veículo: "))

    id = int(ULID())
    modelo_id = str(ULID())
    cor = input("Cor respectiva: ")
    ano_fabricacao = int(input("Ano de fabricação: "))
    ano_modelo = int(input("Ano modelo: "))
    valor = float(input("Valor em R$: "))
    placa = input("Placa do modelo: ").upper()
    vendido = bool(False)

    # UPDATE É UM MÉTODO PARA ATUALIZAR OS VALORES DA MINHA RESPECTIVA CHAVE NO DICIONÁRIO
    dicionarios_veiculos[escolha].update({'id' : id, 'modelo_id' : modelo_id, 'cor' : cor, 'ano_fabricação' : ano_fabricacao, 'ano_modelo' : ano_modelo, 'valor' : valor, 'placa' : placa, 'vendido' : vendido})

    return dicionarios_veiculos

# FUNÇÃO EDITAR E REMOVER
def editar_remover(registro_veiculos):
    print(registro_veiculos)

    remover = input("Deseja remover?(SIM/NAO): ").upper()

    if remover == 'SIM':
        escolha = int(input("Começando no 0, escolha o modelo respectivo para remover: "))
        registro_veiculos.pop(escolha)

        return registro_veiculos
    else:
        pass

    editar = input("Deseja editar?(SIM/NAO): ").upper()

    if editar == 'SIM':
        escolha = int(input("Começando no 0, escolha o modelo respectivo para editar: "))
        id = int(ULID())
        modelo_id = str(ULID())
        cor = input("Cor respectiva: ")
        ano_fabricacao = int(input("Ano de fabricação: "))
        ano_modelo = int(input("Ano modelo: "))
        valor = float(input("Valor em R$: "))
        placa = input("Placa do modelo: ").upper()
        vendido = bool(False)

        # EXCLUO O ANTIGO INDICE DESATUALIZADO E INSIRO UM NOVO INDEX ATUALIZADO NO MESMO LUGAR
        registro_veiculos.pop(escolha)
        registro_veiculos.insert(escolha,{'id' : id, 'modelo_id' : modelo_id, 'cor' : cor, 'ano_fabricação' : ano_fabricacao, 'ano_modelo' : ano_modelo, 'valor' : valor, 'placa' : placa, 'vendido' : vendido}) 

        return registro_veiculos
    else:
        pass

# FUNÇÃO PARA VENDER VEÍCULO
def vende_veiculo(registro_veiculos):
    placa = input("Placa do modelo a ser vendido: ").upper()

    for registro in registro_veiculos:
        if registro["placa"] == placa:
            registro['vendido'] = True
    
    return registro_veiculos

# FUNÇÃO PARA LISTAR VEÍCULOS
def lista_veiculos(registro_geral):
    escolha = input("Listar todos ou filtrar?(TODOS/FILTRAR): ").upper()
    
    if escolha == 'TODOS':
        print('''########## ESCOLHA O ATRIBUTO PARA LISTAR ##########
[1] - Nome modelo
[2] - Ano
[3] - Valor
---------------------------------------------------
''')
    
        atributo = int(input("Escolha uma opção: "))
        tamanho = input("Forma de ordenação(ASC/DESC): ").upper()
        lista = []
        for registro in registro_geral:
            if atributo == 1:
                lista.append(registro["modelo_id"])
            elif atributo == 2:
                lista.append(registro["ano_modelo"])
            elif atributo == 3:
                lista.append(registro["valor"])
        
        if tamanho == 'ASC':
                        for i in range(len(lista)):
                            for j in range(0,len(lista) - i - 1):
                                if lista[j] > lista[j + 1]:
                                    lista[j], lista[j + 1] = lista[j + 1],lista[j]
        else:
            for i in range(len(lista)):
                for j in range(0,len(lista) - i - 1):
                    if lista[j] < lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1],lista[j]
        
        return lista
    else:
        print('''------------ ESCOLHA O FILTRO  ------------
[1] - Parte do nome
[2] - Ano de fabricação
[3] - Ano do modelo
[4] - Valor
[5] - Vendido
[6] - Parte do nome Marca
[7] - Parte do nome Modelo
''')
        
    filtro = int(input("Escolha uma opção: "))
    tamanho = input("Forma de ordenação(ASC/DESC): ").upper()
    lista = []

    for registro in registro_geral:
            if filtro == 1:
                nome = input("Coloque o nome: ").strip()
                if nome in registro:
                    lista.append(registro)
            elif filtro == 2:
                min = int(input("Ano mínimo: "))
                max = int(input("Ano máximo: "))
                if min <= registro["ano_fabricação"] <= max:
                    lista.append(registro)
            elif filtro == 3:
                min = int(input("Ano mínimo: "))
                max = int(input("Ano máximo: "))
                if min <= registro["ano_modelo"] <= max:
                    lista.append(registro)
            elif filtro == 4:
                valor = float(input("Escolha o valor referência: "))
                if registro["valor"] == valor:
                    lista.append(registro)
            elif filtro == 5:
                situacao = input("Você quer os vendidos ou não vendidos?(TRUE/FALSE): ").strip().upper()
                if situacao == 'TRUE':
                    if registro["vendido"] == True:
                        lista.append(registro)
                else:
                    if registro["vendido"] == False:
                        lista.append(registro)
            elif filtro == 6:
                nome = input("Coloque parte do nome do modelo: ").strip()
                if nome in registro["Montadora"]:
                    lista.append(registro)
            elif filtro == 7:
                nome = input("Coloque parte do nome do modelo: ").strip()
                if nome in registro["Montadora"]:
                    lista.append(registro)

    if tamanho == 'ASC':
        for i in range(len(lista)):
            for j in range(0,len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1],lista[j]
    else:
        for i in range(len(lista)):
            for j in range(0,len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1],lista[j]
    
    return lista
