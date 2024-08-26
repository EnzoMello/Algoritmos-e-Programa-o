# Arquivo com as funções que serão usadas na aplicação

from Utils.vetor_utils import criar_vetor_automatico,criar_vetor_manual,carregar_valores_arquivo,multiplica_por_valor,eleva_a_valor,reduzir_a_fracao,substituir_negativo,ordenar_valores,embaralhar_valores,adicionar,remover,remover_posicao,editar_posicao

from Utils.utils import print_tela,number


# Menu principal contendo funções
def main_menu():
    menu = '''

    ================ PLAY NUMBERS ================
    -> Você está no menu inicial do Play Numbers!! Por favor,escolha uma opção:
    [1]- Inicializar vetor numérico.
    [2]- Mostrar todos os valores.
    [3]- Resetar vetor
    [4]- Ver quantidade de itens no vetor
    [5]- Ver Menor e Maior valores e suas posições
    [6]- Somatório dos valores
    [7]- Média dos valores
    [8]- Mostrar Valores positivos e quantidades
    [9]- Mostrar Valores negativos quantidades
    [10]- Atualizar todos os valores escolhendo uma regra
    [11]- Adicionar novos valores
    [12]- Remover itens por valor exato
    [13]- Remover por posição
    [14]- Editar valor específico por posição
    [15]- Salvar valores em arquivo
    [16]- SAIR
    ==============================================
    '''
    return menu
    

# FUNÇÃO OPÇÃO 1
def inicializar_vetor():
    print('''******** INICIANDO VETOR NÚMERICO ********
    1 > Criar vetor automaticamente
    2 > Criar vetor manualmente
    3 > Carregar vetor de um arquivo''')
    
    # PERGUNTA AO USUÁRIO SUA PREFERÊNCIA
    pergunta = int(input("Selecione uma opção: "))


    #VERIFICANDO VALIDADE DA RESPOSTA
    while pergunta != 1 and pergunta != 2 and pergunta != 3:
        print("Resposta inválida.")
        pergunta = int(input("Selecione uma opção: "))

    # VERIFICANDO QUAL OPÇÃO DE VETOR O USUÁRIO ESCOLHEU
    if pergunta == 1:
        vetor_automatico = criar_vetor_automatico()
        print("-" * 25)
        print_tela("Vetor automático criado.")
        return vetor_automatico
    elif pergunta == 2:
        vetor_manual = criar_vetor_manual()
        print("-" * 25)
        print_tela("Vetor manual criado.")
        return vetor_manual
    elif pergunta == 3:
        vetor_carregar = carregar_valores_arquivo()
        print("-" * 25)
        print_tela("Vetor carregado.")
        return vetor_carregar
    else:
        pass

# FUNÇÃO OPÇÃO 2 CRIADA EM VETOR_UTILS.PY


# FUNÇÃO OPÇÃO 3
def resetar_valor(vetor):
    valor_padrao = float(input("Número padrão: "))

    for i in vetor:
        valor_resetado = valor_padrao
        # FUNÇÃO REMOVE FUNCIONA COMO CONTRÁRIA DE APPEND, SÓ NÃO REMOVE APENAS O NÚMERO FINAL DA LISTA.ELA REMOVE QUEM EU QUERO.
        vetor.remove(i)
        vetor.append(valor_resetado)
    print("Elementos resetados.")
     
    return vetor

# FUNÇÃO OPÇÃO 4
def quantidade_itens_vetor(vetor):
    contador = 0

    for i in vetor:
        contador += 1
    
    return contador

# FUNÇÃO OPÇÃO 5
def menor_maior_posicao(vetor):
    menor_valor = 0
    maior_valor = 0
    posicao_menor = 0
    posicao_maior = 0

    for item in vetor:
        # COM O VETOR.INDEX(ITEM), EU ACESSO A POSIÇÃO DO ITEM X DA MINHA LISTA E RETORNO O NMR CORRESPONDETE A ELA
        if vetor.index(item) == 0:
            menor_valor = item
            maior_valor = item
            # O "+ 1" É COLOCADO PARA DAR MAIS SENTIDO NA RESPOSTA AO USUÁRIO, POIS A PRIMEIRA POSIÇÃO EM UMA LISTA É 0 E NÃO 1
            posicao_menor = vetor.index(item) + 1
            posicao_maior = vetor.index(item) + 1
        else:
            if item < menor_valor:
                menor_valor = item
                # MESMA IDEIA DE "+ 1" CITADA ANTERIORMENTE
                posicao_menor = vetor.index(item) + 1
            elif item > maior_valor:
                maior_valor = item
                # MESMA IDEIA DE "+ 1" CITADA ANTERIORMENTE
                posicao_maior = vetor.index(item) + 1
        
    resultado = print('''+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
                      Maior valor = {}
                      Menor valor = {}
                      Posição do maior valor = {} posição
                      Posição do menor valor = {} posição
                      +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''.format(maior_valor,menor_valor,posicao_maior,posicao_menor))
    
    return resultado

# FUNÇÃO OPÇÃO 6
def somatorio_valores(vetor):
    # O SUM É UM MÉTODO QUE JÁ RETORNA A SOMA DOS VALORES EM ALGUM LUGAR
    return sum(vetor)

# FUNÇÃO OPÇÃO 7
def media_valores(soma,vetor):
    return ("Média dos valores: {}".format(soma / vetor))

# FUNÇÃO OPÇÃO 8
def valores_positivos_quantidade(vetor):
    positivos = []
    quantidade = 0

    for numero in vetor:
        if numero > 0:
            positivos.append(numero)
            quantidade += 1
    
    contagem = print("\n Quantidade números positivos = {}".format(quantidade))

    return positivos
    
# FUNÇÃO OPÇÃO 9
def valores_negativos_quantidade(vetor):
    negativos = []
    quantidade_negativos = 0

    for numero in vetor:
        if numero < 0:
            negativos.append(numero)
            quantidade_negativos += 1

    contagem = print("\n Quantidade números negativos = {}".format(quantidade_negativos))

    return negativos

# FUNÇÕES OPÇÕES 10
def menu_atualizacoes(vetor):
    atualizacoes = '''
    ===================== ATUALIZAÇÕES =====================
    (1)-> Multiplicar por um valor
    (2)-> Elevar a um valor (exponenciação)
    (3)-> Reduzir a uma fração 
    (4)-> Substituir valores negativos por um número aleatórios da uma faixa(min, max)
    (5)-> Ordenar valores (reverse)
    (6)-> Embaralhar valores
    ========================================================'''
    
    print_tela(atualizacoes)
    escolhendo = number()

    if escolhendo == 1:
        return multiplica_por_valor(vetor)
    elif escolhendo == 2:
        return eleva_a_valor(vetor)
    elif escolhendo == 3:
        return reduzir_a_fracao(vetor)
    elif escolhendo == 4:
        return substituir_negativo(vetor)
    elif escolhendo == 5:
        return ordenar_valores(vetor)
    elif escolhendo == 6:
        embaralhar_valores(vetor)
    else:
        print("Resposta Inválida.")
        escolhendo = number()

# FUNÇÃO OPÇÃO 11
def adicionar_valores(vetor):
    numero = int(input("Valor a ser adicionado."))
    print("Valor adicionado.")
    return adicionar(vetor,numero)

# FUNÇÃO OPÇÃO 12
def remover_valores(vetor):
    valor = int(input("Valor a ser removido: "))
    print("Análise feita.")
    return remover(vetor,valor)

# FUNÇÃO OPÇÃO 13
def remover_valores_posicao(vetor):
    posicao = int(input("Posição contendo o número a ser removido: "))
    print("Análise concluída.")
    return remover_posicao(vetor,posicao)

# FUNÇÃO OPÇÃO 14
def editar_por_posicao(vetor):
    posicao = int(input("Posição contendo o número a ser editado: "))
    valor_editado = int(input("Como vai ficar o número depois de editado? "))
    print("Edição verificada e adicionada ao final.")
    return editar_posicao(vetor,posicao,valor_editado)

# FUNÇÃO OPÇÃO 15
def salvar_valores_arquivo(vetor):
    print("Salvo na pasta do programa.")
    with open('arquivo.txt', 'w') as arquivo:
        return arquivo.write("Aqui está seu vetor salvo = {}".format(vetor))
    
# FUNÇÃO OPÇÃO 16
def sair(vetor):
    print("PROGRAMA ENCERRADO.")
    with open('arquivo.txt', 'w') as arquivo:
        return arquivo.write("Aqui está seu vetor salvo = {}".format(vetor))