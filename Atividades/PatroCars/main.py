
from funcionalidades_montadores import menu_geral,number_positive,encaminha_crud


def main():
        while True:
            # ESCOLHENDO CRUD
            print(menu_geral())
            escolhe_crud = number_positive()
            encaminha_crud(str(escolhe_crud))

            if escolhe_crud == 0:
                  print("Volte sempre!!!")
                  break
            elif escolhe_crud == 4:
                  saida = input("Pressione uma tecla...")
                  break


main()