# ATIVIDADE DE FATORIAL EM FOR

import random

def main():
    while True:
        print(menu())
        opcao = int(input(" Escolha a opção: "))

        if opcao == 1:
            print("RESULTADO = {}".format(fatorial_n()))
            print("=" * 30)
        elif opcao == 2:
            print("RESULTADO = {}".format(fibonacci()))
            print("=" * 30)
        elif opcao == 3:
            print("Coloque os limites abaixo:")
            print(" Resultado = {}".format(sequencia()), end='')
        elif opcao == 4:
            print("Coloque os numeros abaixo:")
            print("RESULTADO = {}".format(produto_soma()))
            print("=" * 30)
        elif opcao == 5:
            print("Abaixo,coloque número e seu expoente,respectivamente:")
            print("RESULTADO = {}".format(exponencial()))
            print("=" * 30)
        elif opcao == 6:
            print("Coloque os limites abaixo:")
            print("RESULTADO = {}".format(soma_vetor()))
            print("=" * 30)
        elif opcao == 7:
            print("Coloque sua frase abaixo:")
            print("RESULTADO RESPEC. VOGAIS E CONSOANTES = {}".format(vogal_e_consoante()))
            print("=" * 30)
        else:
            print("Programa Encerrado.")
            break

# FUNÇÃO QUE EXIBE UM MENU INICIAL
def menu():
    menu_inicial = '''[1] - Calcular o Fatorial de um número N.
[2] - Imprimir uma Sequência Fibonacci de comprimento C.
[3] - Função que imprime uma Sequência Simples de A até B.
[4] - Calcular o Produto (multiplicação) na forma de somas sucessivas.
[5] - Calcular Exponencial de um Número N elevado a expoente E.
[6] - Dado um intervalo A e B, calcular o somatório de um Vetor de N Elementos Aleatórios.
[7] - Contar Vogais e Consoantes de Frase.'''

    return menu_inicial

# FUNÇÃO QUE CALCULA FATORIAL DE UM NÚMERO N 
def fatorial_n():
    numero = int(input("Qual número para calcular o fatorial: "))
    fatorial = 1

    for elemento in range(numero):
        fatorial *= numero
        numero -= 1

    return fatorial

# FUNÇÃO QUE IMPRIME UMA SEQUÊNCIA FIBONACCI DE COMPRIMENTO C:
def fibonacci():
    C = int(input("Comprimento da sequência: "))
    n1 = 0
    n2 = 1
    final = '{} -> {}'.format(n1, n2)
    
    for numero in range(C):
       n3 = n1 + n2
       final += ' -> {}'.format(n3)
       n1 = n2
       n2 = n3

    return final 

# FUNÇÃO QUE IMPRIME UMA SEQUÊNCIA DE A ATÉ B
def sequencia():
    A, B = input().split()
    lista = []
    if int(A) < int(B):
        min = int(A)
        max = int(B)
    else:
        min = int(B)
        max = int(A)

    for i in range(min,max + 1):
        lista.append(i)

    return lista

# FUNÇÃO QUE CALCULA UM PRODUTO NA FORMA DE SOMAS SUCESSIVAS
def produto_soma():
    A, B = input().split()
    numero_a = int(A)
    calculo = ''

    for _ in range(int(A), int(B)):
        numero_a += int(A)
        calculo += '{} + '.format(A)
    
    calculo += ' = {}'.format(numero_a)

    return calculo

# FUNÇÃO QUE CALCULA EXPONENCIAL DE UM NÚMERO
def exponencial():
    num, exp = input().split()
    expoente = int(exp)
    numero = int(num)
    final = 1

    for _ in range(expoente):
        final *= numero

    return final

# FUNÇÃO QUE SOMA UM VETOR DE ELEMENTOS ALEATÓRIOS EM UM INTERVALO A,B
def soma_vetor():
    A, B = input().split()
    vetor = []
    final = ''

    if int(A) < int(B):
        min = int(A)
        max = int(B)
    else:
        min = int(B)
        max = int(A)

    for elemento in range(max):
        numero = random.randint(min, max)
        vetor.append(numero)

    final += '{} = {}'.format(vetor,sum(vetor))
    return final

# FUNÇÃO QUE CONTA VOGAIS E CONSOANTES DE UMA FRASE
def vogal_e_consoante():
    frase = input().strip().upper()
    vogais = 0
    consoantes = 0

    for caractere in range(len(frase)):
        letra = frase[caractere]
        codigo = ord(letra)

        if codigo == 65 or codigo == 69 or codigo == 73 or codigo == 79 or codigo == 85:
            vogais += 1
        elif codigo > 64 and codigo < 91 and codigo != 65 and codigo != 69 and codigo != 73 and codigo != 79 and codigo != 85:
            consoantes += 1
        
    final = '{} e {}'.format(vogais,consoantes)

    return final

main()