import random

# VARIÁVEIS GLOBAIS QUE AJUDAM A CRIAR ESTADOS INICIAS DAS TORRES E ALTERÁ-LOS AO LONGO DO CÓDIGO
valores_R = None
valores_G = None
valores_B = None
nivel_jogo = None

def main():
    contador_1 = 0
    contador_2 = 0
    rodada = 1
    global valores_R,valores_G,valores_B,nivel_jogo

    # ESCLARECENDO A SITUAÇÃO PARA O USUÁRIO
    print(objetivo())
    print("~"* 140)

    print(menu())
    escolher_nivel = escolha_feita()
    nivel_jogo = escolher_nivel

    while True:
        # MENU DA OPÇÃO ESCOLHIDA
        print(estados())
        # CHAMA A FUNÇÃO DE ESCOLHA
        escolher = escolha_feita()
        if escolher == 1:
            print("\033[0;33mDiga as torres logo abaixo.\033[m")
            if rodada == 1:
                contador_1 += 1
            elif rodada == 2:
                contador_2 += 1
            
            transferencias()

        elif escolher == 2:
            print("\033[0;33mVocê optou por ENCERRAR o programa,até breve!!\033[m")
            break

        if 'B' not in valores_R and 'B' not in valores_G and 'G' not in valores_R and 'G' not in valores_B and 'R' not in valores_B and 'R' not in valores_G:
            valores_R = valores_G = valores_B = None
            rodada += 1

        if rodada == 3:
            print("JOGADOR 1: {} pontos".format(contador_1))
            print("JOGADOR 2: {} pontos".format(contador_2))

            if contador_1 > contador_2:
                print("\033[0;32mVENCEDOR FOI O JOGADOR 1\033[m")
            elif contador_2 > contador_1:
                print("\033[0;32mVENCEDOR FOI O JOGADOR 2\032[m")
            else:
                print("\033[0;32mTEMOS UM EMPATE!!!\032[m")




# FUNÇÃO SOBRE O OBJETIVO DO JOGO
def objetivo():
    esclarecendo = " \033[0;34mSeja bem-vindo, você possui três torres(R,G e B),sendo que R está completamente cheia de itens enquanto as outras duas estão vazias.\n Você deve fazer transferências de itens entre as torres, de modo a cada torre ter apenas itens de sua letra. \n Vence o jogador com menos rodadas para atingir o objetivo.\033[m"
    return esclarecendo

# FUNÇÃO COM MENU DO JOGO
def menu():
    menu_inicial = '''     \033[0;34m------------------> MODOS DE JOGO <--------------------\033[m
    \033[0;34m[1] -> Nível Básico\033[m
    \033[0;34m[2] -> Nível Intermediário\033[m
    \033[0;34m[3] -> Nível Avançado\033[m
    \033[0;34m-------------------------------------------------\033[m
    '''.format()

    return menu_inicial

# FUNÇÃO QUE MOSTRA OS ESTADOS DAS TORRES DE ACORDO COM O NÍVEL ESCOLHIDO
def estados():
    global valores_R,valores_G,valores_B

    menu_inicial = '''     \033[0;35m------------------> ESTADO ATUAL <--------------------\033[m
    Torre R = \033[0;34m{}\033[m       
    Torre G = \033[0;31m{}\033[m     
    Torre B = \033[0;33m{}\033[m
    \033[0;35m-------------------------------------------------\033[m
    \033[0;35mESCOLHAS POSSÍVEIS:\033[m
    \033[0;35m[1] -> Realizar operação entre as torres\033[m
    \033[0;35m[2] -> SAIR\033[m
    '''.format(torre_r(),torre_g(),torre_b())

    return menu_inicial

# FUNÇÃO PARA O USUÁRIO ESCOLHER
def escolha_feita():
    escolha = int(input("\033[0;33mQual opção desejada? \033[m"))
    
    if escolha != 1 and escolha != 2 and escolha != 3:
        print("\033[0;35mEscolha inválida.\033[m")
        escolha = int(input("\033[0;35mTente de novo:\033[m"))

    return escolha

# FUNÇÃO QUE CRIA TORRE R COMPLETA COM OS 9 ITENS
def torre_r():
    # TORNO GLOBAL A MINHA VARIÁVEL DE VALORES_R E ASSIM CONSIGO ATRIBUIR VALOR A UMA VARIÁVEL FORA DA FUNÇÃO
    global valores_R

    if valores_R is None:
        vetor_r = []
        lista = [66,71,82]

        for letra in range(9):
            letra_sorteada = random.choice(lista)
            vetor_r.append(chr(letra_sorteada))
        # MINHA VARIÁVEL GLOBAL VALORES_R PASSA A SER O VETOR_R CRIADO, ASSIM A FUNÇÃO NÃO GERA UM VETOR NOVO A CADA VEZ QUE É CHAMADA
        valores_R = vetor_r
            

    return valores_R

# FUNÇÃO QUE CRIA TORRE G VAZIA
def torre_g():
    # TORNO GLOBAL A MINHA VARIÁVEL DE VALORES_G E ASSIM CONSIGO ATRIBUIR VALOR A UMA VARIÁVEL FORA DA FUNÇÃO
    global valores_G,nivel_jogo
    vetor_g = []

    if valores_G is None:
        # VERIFICANDO O NÍVEL DE JOGO ESCOLHIDO E AJUSTANDO MEU VETOR PARA ATENDER ESSE TIPO
        if nivel_jogo == 1:
            valores_G is None
            valores_G = vetor_g
        elif nivel_jogo == 2:
            lista = [66,71,82]
            for letra in range(3):
                letra_sorteada = random.choice(lista)
                vetor_g.append(chr(letra_sorteada))
                valores_G = vetor_g
        elif nivel_jogo == 3:
            lista = [66,71,82]
            for letra in range(9):
                letra_sorteada = random.choice(lista)
                vetor_g.append(chr(letra_sorteada))
                valores_G = vetor_g
        
    return valores_G

# FUNÇÃO QUE CRIA TORRE B VAZIA
def torre_b():
    # TORNO GLOBAL A MINHA VARIÁVEL DE VALORES_B E ASSIM CONSIGO ATRIBUIR VALOR A UMA VARIÁVEL FORA DA FUNÇÃO
    global valores_B,nivel_jogo
    vetor_b = []
    
    if valores_B is None:
        # VERIFICANDO O NÍVEL DE JOGO ESCOLHIDO E AJUSTANDO MEU VETOR PARA ATENDER ESSE TIPO
        if nivel_jogo == 1:
            valores_B is None
            valores_B = vetor_b
        elif nivel_jogo == 2:
            lista = [66,71,82]
            for letra in range(3):
                letra_sorteada = random.choice(lista)
                vetor_b.append(chr(letra_sorteada))
                valores_B = vetor_b
        elif nivel_jogo == 3:
            lista = [66,71,82]
            for letra in range(8):
                letra_sorteada = random.choice(lista)
                vetor_b.append(chr(letra_sorteada))
                valores_B = vetor_b
        
    return valores_B

# FUNÇÃO QUE VAI FAZER TRANSFERÊNCIAS ENTRE AS MINHAS TORRES
def transferencias():
    global valores_R,valores_G,valores_B

    # DICIONÁRIO PARA IDENTIFICAR LOCAL DE RETIRADA E LOCAL DE INCREMENTO
    dicionario = {
        'R' : valores_R,
        'G' : valores_G,
        'B' : valores_B
        }

    while True:
        operacao = input().upper()
        
        if len(operacao) != 2:
            print("Operação inválida,tente novamente.")
            continue

        partindo = operacao[0]
        chegando = operacao[1]

        if partindo not in dicionario or chegando not in dicionario:
            print("Tente novamente com 'R', 'G' ou 'B'.")
            continue

        # IDENTIFICA A TORRE A PEGAR O ELEMENTO DO TOPO E ADICIONA NO TOPO DA RESPECTIVA TORRE ESCOLHIDA
        retirada = dicionario[partindo]
        incrementada = dicionario[chegando]
        
        # IDENTIFICANDO EXCEÇÕES DE TRANSFERÊNCIAS E POSSIBILITANDO A TRANSFERÊNCIA EM CASO DE ESTAR TUDO OK
        if len(retirada) == 0:
            print("A torre de retirada tem 0 itens.Você pode apenas adicionar itens nela,por enquanto.T ente novamente.")
        elif len(incrementada) == 9:
            print("Essa torre está cheia.Você pode apenas remover itens dela,por enquanto. Tente novamente.")
        elif partindo == chegando:
            print("Você está querendo transferir para mesma torre de retirada, não é válido esse movimento. Tente novamente")
        else:
            item = retirada.pop()
            incrementada.append(item)
            # ATUALIZA AS VARIÁVEIS GLOBAIS APÓS TRANSFERÊNCIAS
            valores_R,valores_G,valores_B = dicionario['R'],dicionario["G"],dicionario["B"]
            break
            
        # COMO ESTOU USANDO VARIÁVEIS GLOBAIS, NÃO PRECISO RETORNAR NADA. ELAS JÁ SÃO ALTERADAS PELO MEU ESCOPO DA FUNÇÃO 





















































main()