def main():
    # IMPLEMENTAÇÃO COM EXEMPLO DE BUSCA DE UM ELEMENTO EM UM VETOR DE NÚMEROS N,PORÉM A LISTA PRECISA ESTAR ORDENADA
    meu_vetor = criar_vetor()
    vetor_ordenado = quick_sort(meu_vetor)
    valor = int(input("Informe o elemento a ser encontrado: "))
    busca_resultado = busca_binaria(vetor_ordenado,valor)
    
    print("\033[0;33m{}".format(vetor_ordenado))
    if busca_resultado != -1:
        print("\033[0;34mO elemento {} se encontra na posição {}".format(valor,busca_resultado))
    else:
        print("\033[0;34mElemento não encontrado")

def criar_vetor():
    lista = []
    n = int(input("Coloque o limite N: "))

    for numero in range(1,n + 1):
        algarismo = int(input("Elemento a adicionar: "))
        lista.append(algarismo)
    
    return lista

def busca_binaria(vetor_exemplo,valor_exemplo):
    left = 0
    right = len(vetor_exemplo) - 1

    # PARA CADA VALOR NO MEU VETOR, VOU "EMPURRANDO" PARA ESQUERDA OS MENORES E OS MAIORES PARA A DIREITA,ATÉ ACHAR A POSIÇÃO DO VALOR ESCOLHIDO
    while left <= right:
        meio = (left + right) // 2
        if vetor_exemplo[meio] == valor_exemplo:
            return meio + 1
        elif vetor_exemplo[meio] < valor_exemplo:
            left = meio + 1
        else:
            right = meio - 1
    
    return -1

# QUICK SORT VAI ORDENAR A MINHA LISTA E ASSIM MINHA FUNÇÃO BUSCA BINÁRIA SE TORNA 100% EFETIVA
def quick_sort(vetor_exemplo):
    
    if len(vetor_exemplo) < 2:
        return vetor_exemplo
    else:
        # LIST COMPREHENSION POUPA DE EXTENDER O CÓDIGO COM FOR
        pivo = vetor_exemplo[0]
        left = [elemento for elemento in vetor_exemplo[1:] if elemento <= pivo]
        right = [elemento for elemento in vetor_exemplo[1:] if elemento > pivo]

    
    # RETORNANDO EM UMA LINHA ORDENADA COM OS VALORES DO MEU VETOR
    return quick_sort(left) + [pivo] + quick_sort(right)
main()