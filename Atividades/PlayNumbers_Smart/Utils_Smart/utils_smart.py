# Arquivo contendo funções de entrada e saída de dados,que serão usados na aplicação

# Função para printar algo na minha tela
def print_tela(texto):
    print(texto)

# Função para pedir um número
def number():
    digito = float(input("Digite um número: "))
    return digito

# Função para pedir um número positivo
def number_positive(digito):
    digito = int(input("Digite um número positivo: "))

    while digito < 0:
        print("Número inválido.")
        digito = int(input("Digite um número positivo: "))

    if digito > 0:
        return digito
    
# Função para pedir número negativo
def negative_number(digito):
    digito = int(input("Digite número negativo: "))

    while digito > 0:
        print("Número inválido!")
        digito = int(input("Digite um número negativo: "))

    if digito < 0:
        return digito
    
# Função com número máximo
def number_max():
    digito = int(input("Número máximo possível: "))
    return digito

#Função com número mínimo
def number_min():
    digito = int(input("Número mínimo possível: "))
    return digito