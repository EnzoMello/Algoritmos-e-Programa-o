def main():
    # IMPLEMENTAÇÃO COM EXEMPLO DE BUSCA DE UM ELEMENTO EM UM VETOR DE NÚMEROS N
    meu_vetor = criar_vetor()
    valor = input("Informe o elemento a ser encontrado: ")
    busca_resultado = busca_linear(meu_vetor,valor)

    if busca_resultado != -1:
        print("\033[0;34mO elemento {} se encontra na posição {}".format(valor,busca_resultado))
    else:
        print("\033[0;34mElemento não encontrado")

# FUNÇÃO QUE CRIA UM VETOR COM UM TAMANHO DA MINHA PREFERÊNCIA
def criar_vetor():
    lista = []
    n = int(input("Coloque o limite N: "))

    for numero in range(n):
        algarismo = input("Elemento a adicionar: ").upper()
        lista.append(algarismo)
    
    return lista
    
# FUNÇÃO QUE VERIFICA EM QUE POSIÇÃO MEU NÚMERO SE ENCONTRA
def busca_linear(vetor_exemplo,valor_exemplo):
    for elemento in range(len(vetor_exemplo)):
        if vetor_exemplo[elemento].upper() == valor_exemplo.upper():
            return elemento + 1
        
    return -1
        
main()
