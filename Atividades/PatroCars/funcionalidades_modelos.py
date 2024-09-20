from ulid import ULID

## UTILS PARA CRUD MODELO DE VEICULOS
# FUNÇÃO PARA ADICIONAR MODELO DE VEÍCULO
def adicionar_modelo(registro_geral):
    
    registro_modelos = []
    print(registro_geral)
    escolha = int(input("Os números referentes às montadoras começam no 0, selecione uma: "))

    while registro_geral[escolha] not in registro_geral:
        escolha = int(input("Os números referentes às montadoras começam no 0, selecione uma: "))

    id_modelo = int(ULID())
    nome_modelo = input("Nome do modelo: ").upper()
    valor_ref = float(input("Valor de referência: "))
    motorizacao = int(input("Valor de motorização: "))
    turbo = bool(input("Tem turbo?(True/False): "))
    automatico = bool(input("É automático?(Sim/Não): "))

    registro_modelos.append({"Montadora": registro_geral[escolha]["nome"], "id_modelo" : id_modelo, "nome_modelo" : nome_modelo, "valor_ref" : valor_ref, "motorização" : motorizacao, "turbo" : turbo, "automatico" : automatico})

    return registro_modelos



# FUNÇÃO PARA LISTAR MODELOS
def lista_modelos(registro_geral):
    preferencia = input("Prefere escolher montadora ou listar todos os modelos?(Escolher/Listar todos) ").upper().strip()
    print('''########## ESCOLHA O ATRIBUTO PARA LISTAR ##########
[1] - Nome modelo
[2] - Automático ou Não
[3] - Motor
[4] - Nome da montadora
---------------------------------------------------
''')
    
    atributo = int(input("Escolha uma opção: "))
    tamanho = input("Forma de ordenação(ASC/DESC): ").upper()

    if preferencia == "ESCOLHER":
        modelos = []
        print(registro_geral)
        escolha = input("Coloque o nome da montadora: ")

        for registro in registro_geral:
            if escolha == registro["Montadora"]:
                if atributo == 1:
                    modelos.append(registro["nome_modelo"])
                elif atributo == 2:
                    modelos.append(registro["automatico"])
                elif atributo == 3:
                    modelos.append(registro["motorização"])
                elif atributo == 4:
                    modelos.append(registro)
                else:
                    print("Atributo inválido.")
        
        if tamanho == 'ASC':
                        for i in range(len(modelos)):
                            for j in range(0,len(modelos) - i - 1):
                                if modelos[j] > modelos[j + 1]:
                                    modelos[j], modelos[j + 1] = modelos[j + 1],modelos[j]
        else:
            for i in range(len(modelos)):
                for j in range(0,len(modelos) - i - 1):
                    if modelos[j] < modelos[j + 1]:
                        modelos[j], modelos[j + 1] = modelos[j + 1],modelos[j]
        
        return modelos
    else:
        modelos = []
        print(registro_geral)
        for registro in registro_geral:
            if atributo == 1:
                modelos.append(registro["nome_modelo"])
            elif atributo == 2:
                modelos.append(registro["Montadora"])
            elif atributo == 3:
                modelos.append(registro["valor_ref"])
            elif atributo == 4:
                modelos.append(registro["motorização"])
            else:
                print("Atributo inválido.")
        
        if tamanho == 'ASC':
                        for i in range(len(modelos)):
                            for j in range(0,len(modelos) - i - 1):
                                if modelos[j] > modelos[j + 1]:
                                    modelos[j], modelos[j + 1] = modelos[j + 1],modelos[j]
        else:
            for i in range(len(modelos)):
                for j in range(0,len(modelos) - i - 1):
                    if modelos[j] < modelos[j + 1]:
                        modelos[j], modelos[j + 1] = modelos[j + 1],modelos[j]
        return modelos

# FUNÇÃO PARA REMOVER MODELOS
def remover_modelos(registro_geral):
    print(registro_geral)

    escolha = int(input("A primeira montadora é a número 0, selecione qual deseja excluir: "))
    registro_geral.pop(escolha)

    return registro_geral

# FUNÇÃO PARA EDITAR MODELOS DE VEÍCULOS
def editar_modelos(registro_geral):
    print(registro_geral)

    escolha = int(input("A primeira montadora é a número 0, selecione qual deseja editar: "))
    escolha_atributo = input("Digite qual o nome da chave respectiva que é para editar(começa pela 0): ")
    novo_valor = input("Nova valor para chave(0 não altera): ")

    registro_geral[escolha][escolha_atributo] = novo_valor

    return registro_geral
