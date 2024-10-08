# ATIVIDADE DE FATORIAL EM FUNÇÃO RECURSIVA

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
            print(" Resultado = {}".format(sequencia()))
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
    
    return fatorial_recursivo(numero)

# FUNÇÃO RECURSIVA PARA FATORIAL
def fatorial_recursivo(numero_exemplo):
    return numero_exemplo * fatorial_recursivo(numero_exemplo - 1)

# FUNÇÃO QUE IMPRIME UMA SEQUÊNCIA FIBONACCI DE COMPRIMENTO C:
def fibonacci():
    C = int(input("Comprimento da sequência: "))

    return fibonacci_recursiva(0,1,C,0,"")
    
# FUNÇÃO RECURSIVA PARA FIBONACCI
def fibonacci_recursiva(n1, n2, c_exemplo, contador, final):
    if contador >= c_exemplo - 2:
        return final
    
    n3 = n1 + n2 
    final += "-> {} ".format(n3)
    
    return fibonacci_recursiva(n2,n3,c_exemplo,contador + 1, final)

# FUNÇÃO QUE IMPRIME UMA SEQUÊNCIA DE A ATÉ B
def sequencia():
    A, B = map(int, input().split())
    minimo = min(A, B)
    maximo = max(A, B)
    
    return sequencia_recursiva(minimo,maximo,"")

# FUNÇÃO RECURSIVA PARA SEQUÊNCIA A ATÉ B
def sequencia_recursiva(min_,max_,resultado):
    if min_ > max_:
        return resultado
    
    resultado += "{} ".format(min_)

    return sequencia_recursiva(min_ + 1,max_,resultado)

# FUNÇÃO QUE CALCULA UM PRODUTO NA FORMA DE SOMAS SUCESSIVAS
def produto_soma():
    A, B = map(int,input().split())
    
    return produto_recursivo(A,B)

# FUNÇÃO RECURSIVA PARA PRODUTO DE FORMA SOMA SUCESSIVA
def produto_recursivo(valor1,valor2):
    if valor2 == 0:
        return 0
    elif valor1 < 0:
        return -valor1 + produto_recursivo(valor1,valor2 + 1)
    else:
        return valor1 + produto_recursivo(valor1,valor2 - 1)

# FUNÇÃO QUE CALCULA EXPONENCIAL DE UM NÚMERO
def exponencial():
    num, exp = map(int,input().split())
    
    return exponencial_recursivo(num, exp)

# FUNÇÃO RECURSIVA PARA EXPONENCIAL
def exponencial_recursivo(valor1, valor2):
    if valor2 == 0:
        return 1
    return valor1 * exponencial_recursivo(valor1,valor2 - 1)

# FUNÇÃO QUE SOMA UM VETOR DE ELEMENTOS ALEATÓRIOS EM UM INTERVALO A,B
def soma_vetor():
    A, B = map(int, input().split())
    
    # PEDINDO QNTD DE ELEMENTOS NO VETOR
    n = int(input("Quantidade de elementos no vetor N: "))
    vetor = []
    for _ in range(n):
        vetor.append(random.randint(A,B))

    resultado = soma_vetor_recursivo(vetor)
    
    return resultado

# FUNÇÃO RECURSIVA PARA SOMAR ELEMENTOS DO VETOR
def soma_vetor_recursivo(vetor_):
    if not vetor_:
        return 0
    else:
        return vetor_[0] + soma_vetor_recursivo(vetor_[1:])
    

# FUNÇÃO QUE CONTA VOGAIS E CONSOANTES DE UMA FRASE
def vogal_e_consoante():
    frase = input().strip().upper()
    return recursiva_vogal_consoante(frase,0,0,0)

# FUNÇÃO RECURSIVA PARA VOGAL E CONSOANTE
def recursiva_vogal_consoante(frase,index,vogais,consoantes):
    if index >= len(frase):
        return '{} e {}'.format(vogais,consoantes)
    letra = frase[index]
    codigo = ord(letra)
    if codigo in (65,69,73,79,85):
        vogais += 1
    elif codigo >= 65 and codigo <= 90:
        consoantes +=1
    
    return recursiva_vogal_consoante(frase,index + 1,vogais,consoantes)

main()