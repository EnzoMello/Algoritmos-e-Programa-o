# Arquivo principal, contendo o Menu de aplicações e as funções das funcionalidades

from Utils.vetor_funcionalidades import main_menu,inicializar_vetor,resetar_valor,quantidade_itens_vetor,menor_maior_posicao,somatorio_valores,media_valores,valores_positivos_quantidade,valores_negativos_quantidade,menu_atualizacoes,adicionar_valores,remover_valores,remover_valores_posicao,editar_por_posicao,salvar_valores_arquivo,sair

from Utils.vetor_utils import mostrar_vetor

from Utils.utils import number

def main():
    while True:
        # Menu de opções para o usuário 
        print(main_menu())
        escolha = number()
        # Usuário escolhe a opção
        if escolha == 1:
            escolha_feita = inicializar_vetor()
        elif escolha == 2:
            mostrar_vetor(escolha_feita,escolha)
        elif escolha == 3:
            valor_resetado = resetar_valor(escolha_feita)
        elif escolha == 4:
            mostrar_vetor(quantidade_itens_vetor(escolha_feita),escolha)
        elif escolha == 5:
            print(menor_maior_posicao(escolha_feita))
        elif escolha == 6:
            print(somatorio_valores(escolha_feita))
        elif escolha == 7:
            print(media_valores(somatorio_valores(escolha_feita),quantidade_itens_vetor(escolha_feita)))
        elif escolha == 8:
            print(valores_positivos_quantidade(escolha_feita))
        elif escolha == 9:
            print(valores_negativos_quantidade(escolha_feita))
        elif escolha == 10:
            print(menu_atualizacoes(escolha_feita))
        elif escolha == 11:
            print(adicionar_valores(escolha_feita))
        elif escolha == 12:
            print(remover_valores(escolha_feita))
        elif escolha == 13:
            print(remover_valores_posicao(escolha_feita))
        elif escolha == 14:
            print(editar_por_posicao(escolha_feita))
        elif escolha == 15:
            print(salvar_valores_arquivo(escolha_feita))
        elif escolha == 16:
            print(sair(escolha_feita))
            break
        else:
            print("Escolha inválida")

main()