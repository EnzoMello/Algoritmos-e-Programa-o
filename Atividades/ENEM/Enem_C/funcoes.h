#ifndef FUNCOES_H  // Evita inclusões duplicadas
#define FUNCOES_H

// Constantes úteis para leitura do arquivo CSV
#define MAX_LINHA 800
#define MAX_NOME 150
#define MAX_ENTRADAS 16000

// Declaração da estrutura Escola
typedef struct {
    char nome[MAX_NOME];
    float nota;
} Escola;

// Declarações de funções
const char* menu_principal();
void top_brasil(int top);
int comparar(const void *a, const void *b);

#endif
