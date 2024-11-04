#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funcoes.h"

// CONSTANTES ÚTEIS PARA LEITURA DO ARQUIVO CSV
#define MAX_LINHA 800
#define MAX_NOME 150
#define MAX_ENTRADAS 16000

const char* menu_principal(){
    // STATIC PERMITE QUE O ESPAÇO ALOCADO PARA MENU PERSISTA ENTRE MEMÓRIAS E NÃO ME PREOCUPE COM ALOCAÇÃO SEMPRE QUE PRECISE DA FUNÇÃO DE MENU
    static char menu[1000];
    // SNPRINTF ME AJUDA A LIMITAR O TAMANH0 DA MINHA STRING, PARA QUE NÃO ULTRAPASSE O LIMITE ESTABELECIDO
    snprintf(menu, sizeof(menu),
    "<------------------------------------------> CONSULTAS ENEM <--------------------------------------------------------------->\n"
    "[1] -> TOP N BRASIL (TODAS AS ÁREAS)        | [5] -> MÉDIA NACIONAL POR ÁREA                                |  [9] -> RANKING ENEM POR ESTADO\n"
    "[2] -> TOP BRASIL POR ÁREA                  | [6] -> MELHOR ESCOLA POR ÁREA E ESTADO OU BR                  |  [10] -> RANKING ENEM P/REGIÃO PAÍS\n"
    "[3] -> TOP BRASIL POR ESTADO                | [7] -> LISTAR ESCOLAS POR ESTADO ORDENADO POR RENDA           |  \n"
    "[4] -> TOP BRASIL POR ESTADO E REDE         | [8] -> BUSCA ESCOLA ESPECÍFICA POR PARTE DO NOME              |  [0] = SAIR\n"
    "<--------------------------------------------------------------------------------------------------------------------------------------------------->\n");

return menu;
}

// -> CONSTRUINDO A OPÇÃO 1:


// EM PYTHON, FOI POSÍVEL ORDENAR DECRESCENTEMENTE USANDO SORTED. PORÉM, AQUI NO C É PRECISO CRIAR UMA FUNÇÃO PARA ORDENAR
int comparar(const void *a, const void *b){ // Uma função que tem ponteiros void como parâmetro, permitindo receber qualquer valor para comparar.
    Escola *escolaA = (Escola*)a;
    Escola *escolaB = (Escola*)b; // variáveis que são ponteiros para struct do tipo Escola, permitindo acessar nota e nome.

    if (escolaB->nota > escolaA->nota) return 1;
    if (escolaB->nota < escolaA->nota) return -1; // Função vai ordenar as notas decrescentemente.
    return 0;
}

void top_brasil(int top){
    FILE *arquivo = fopen("planilha.txt.csv", "r");
    if(!arquivo){
        puts("Erro ao abrir arquivo.\n");
        return;
    }
    puts("Arquivo aberto com sucesso\n");

    Escola ranking[MAX_ENTRADAS]; // O máximo de entradas no meu array
    int count = 0;
    char linha[MAX_LINHA]; // O tamanho máximo de caracteres em cada linha

    while (fgets(linha, sizeof(linha), arquivo)){ // Inicia um loop que lê cada linha do arquivo até seu final
        char *coluna = strtok(NULL, ";");  // STRTOK SERVE PARA DIVIDIR A LINHA EM COLUNAS, USANDO ";"" COMO DELIMITADOR
        int colunaAtual = 0;
        Escola escolaAtual;

        while (coluna != NULL){
            // VERIFICANDO AS COLUNAS E ADICIONANDO NOME E NOTA
            if(colunaAtual == 1){
                strncpy(escolaAtual.nome, coluna, MAX_NOME);
                escolaAtual.nome[MAX_NOME - 1] = '\0';
            }

            if(colunaAtual == 12){
                escolaAtual.nota = strtof(coluna, NULL); // STRTOF CONVERTE STRING PARA FLOAT, JÁ QUE NO ARQUIVO CSV AS NOTAS ESTÃO COMO STRING
                break;
            }
            coluna = strtok(NULL, ";");
            colunaAtual++;

        }

        if (count < MAX_ENTRADAS){
            ranking[count++] = escolaAtual;
        }
    }

    fclose(arquivo);

    // Ordenar o ranking em ordem decrescente
    qsort(ranking, count, sizeof(Escola), comparar); // Aplica o Quick Sort. Ranking é o ponteiro para início do array, count é o numero de elementos a serem lidos, sizeof é o tamanho dos elementos a serem lidos e comparar é a função de comparação

    printf("Top %d Escolas:\n", top);
    for(int i = 0; i < top && i < count; i++){
        printf("%d lugar -> %s - Nota: %.2f\n", i+1, ranking[i].nome, ranking[i]. nota);
    }

}

