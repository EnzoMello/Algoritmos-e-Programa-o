# Arquivo contendo funções específicas para manipulação de vetores na aplicação

from Utils_Smart.utils_smart import number_max,number_min
import random 

vetor_global = []


# MANIPULAÇÃO DA OPÇÃO 1:
## EM CASO DE VETOR AUTOMÁTICO
def criar_vetor_automatico():
    # PEDINDO UM TAMANHO, LIMITE MÁXIMO E LIMITE MÍNIMO DO VETOR
    tamanho_vetor = int(input("Quantos elementos você quer no vetor? "))
    maximo = number_max()
    minimo = number_min()
    
    vetor_cliente = []

    for elemento in range(tamanho_vetor):
        # A BIBLIOTECA RANDOM TEM A FUNÇÃO UNIFORM,QUE SORTEA UM NÚMERO ALEATÓRIO DENTRO DE UM INTERVALO FLOAT
        numero_sorteado = random.randint(minimo, maximo)
        # ADICIONO COM O APPEND O NÚMERO SORTEADO NA LISTA DE VETORES. DETALHE: ELE JÁ ENTRA FORMATADO
        vetor_cliente.append(numero_sorteado)

    return vetor_cliente

## EM CASO DE VETOR MANUAL
def criar_vetor_manual():
    # PEDINDO UM TAMANHO, LIMITE MÁXIMO E LIMITE MÍNIMO DO VETOR
    tamanho_vetor = int(input("Quantos elementos você deseja informar? "))
    maximo = number_max()
    minimo = number_min()

    vetor_manual_cliente = []

    for elemento in range(tamanho_vetor):
        novo_valor = float(input("Digite o valor que você quer computar: "))

        # VERIFICANDO SE O NÚMERO DIGITADO ESTÁ DENTRO DOS LIMITES
        if novo_valor >= minimo and novo_valor <= maximo:
            vetor_manual_cliente.append(novo_valor)
        else:
            print("Valor inválido,tente de novo")
            novo_valor = float(input("Digite o valor que você quer computar: "))

    return vetor_manual_cliente

## EM CASO DE CARREGAR UM ARQUIVO
def carregar_valores_arquivo():
    nome_do_arquivo = input("Por favor,digite o nome do arquivo a carregar os valores: ")
    arquivo = open('{}'.format(nome_do_arquivo))

    vetor_carregado = []

    with open('{}'.format(nome_do_arquivo), 'r') as arquivo:
        linhas = arquivo.readlines()
        vetor_carregado.append(linhas)  

    return vetor_carregado 


# MANIPULAÇÃO DA OPÇÃO 2:
def mostrar_vetor(valores,opcao):
    if opcao != 4:
        print("Valores no vetor = {}".format(valores))
    elif opcao == 6:
        print("Soma dos valores no vetor = {}".format(valores))
    else:
        print("Quantidade de itens = {}".format(valores))

# MANIPULAÇÃO DA OPÇÃO 10:
def multiplica_por_valor(vetor):
    valor = float(input("Valor usado na multiplicação: "))

    return list(map(lambda x: x * valor, vetor))


def eleva_a_valor(vetor):
    valor = int(input("Valor para elevação: "))

    return list(map(lambda x: x**valor, vetor))

def reduzir_a_fracao(vetor):
    numerador = int(input("Numerador da fração: "))
    denominador = int(input("Denominador da fração: "))
    
    return list(map(lambda x: ( x * numerador) / denominador,vetor))

def substituir_negativo(vetor):
    minimo = int(input("Limite mínimo do intervalo: "))
    maximo = int(input("Limite máximo do intervalo: "))

    for elemento in range(len(vetor)):
        if vetor[elemento] < 0:
            sorteia_numero = random.randint(minimo,maximo)
            vetor.remove(elemento)
            vetor.append(sorteia_numero)

    return vetor

def ordenar_valores(vetor):
    tipo_ordenacao = input("Deseja ordenar crescente ou decrescentemente? ").upper()
    defin_temporaria = input("Deseja ordenar definitivamente ou temporariamente? ").upper()

    # SORT SERVE PARA ORDENAR DEFINITIVAMENTE OS ELEMENTOS DA LISTA E SORTED RETORNA UMA NOVA LISTA ORDENADA, DEIXANDO A ORIGINAL INALTERADA
    if tipo_ordenacao == 'CRESCENTE' and defin_temporaria == 'DEFINITIVAMENTE':
        vetor.sort()
        return vetor
    # REVERSE SERVE PARA ORDENAR DECRESCENTEMENTE
    elif tipo_ordenacao == 'DECRESCENTEMENTE' and defin_temporaria == 'DEFINITIVAMENTE':
        vetor.sort(reverse = True)
        return vetor
    elif tipo_ordenacao == 'CRESCENTE' and defin_temporaria == 'TEMPORARIAMENTE':
        novo_vetor = sorted(vetor)
        return novo_vetor
    else:
        novo_vetor = sorted(vetor, reverse = True)
        return novo_vetor

def embaralhar_valores(vetor):
    # TUDO NESSA FUNÇÃO PODERIA SER SIMPLIFICADO USANDO RANDOM.SHUFFLE(), QUE É UM MÉTODO PARA EMBARALHAR ELEMENTOS
    embaralhamento = random.shuffle(vetor)

    return embaralhamento

# MANIPULAÇÃO OPÇÃO 11
def adicionar(vetor,valor):
    vetor.append(valor)
    return vetor

# MANIPULAÇÃO OPÇÃO 12
def remover(vetor,valor):
    for elemento in vetor:
        if elemento == valor:
            vetor.remove(elemento)

    return vetor

# MANIPULAÇÃO OPÇÃO 13
def remover_posicao(vetor, algarismo):
    minha_lista = vetor

    for elemento in minha_lista:
        if minha_lista.index(elemento) == algarismo:
            minha_lista.remove(elemento)

    return minha_lista

# MANIPULANDO OPÇÃO 14
def editar_posicao(vetor,algarismo,editado):
    minha_lista = vetor

    for elemento in minha_lista:
        if minha_lista.index(elemento) == algarismo:
            minha_lista.remove(elemento)
            minha_lista.append(editado)

    return minha_lista