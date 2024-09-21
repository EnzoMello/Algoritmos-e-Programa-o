from funcoes_enem import menu_principal,top_brasil,top_area,top_estado,top_estado_rede,media_nacional_area,melhor_escola,lista_ordenada_renda,busca_escola,ranking_estado,ranking_regiao

def main():
    while True:
        print(menu_principal())
        escolha = int(input("Escolha: "))

        if escolha == 1:
            print(top_brasil())
        elif escolha == 2:
            print(top_area())
        elif escolha == 3:
            print(top_estado())
        elif escolha == 4:
            print(top_estado_rede())
        elif escolha == 5:
            print(media_nacional_area())
        elif escolha == 6:
            print(melhor_escola())
        elif escolha == 7:
            print(lista_ordenada_renda())
        elif escolha == 8:
            print(busca_escola())
        elif escolha == 9:
            print(ranking_estado())
        elif escolha == 10:
            print(ranking_regiao())
        elif escolha == 0:
            break
main()
