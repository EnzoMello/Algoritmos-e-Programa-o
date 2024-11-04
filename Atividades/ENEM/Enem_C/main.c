#include <stdio.h>
#include <string.h>
#include "funcoes.h"


int main(){
    while (1){
        const char* menu = menu_principal();
        printf("%s", menu);
        
        char escolha[10];
        int top;
        puts("Coloque sua escolha abaixo e o top N escolas a comparar: ");
        scanf("%s", escolha);
        scanf("%d", &top);

        if(strcmp(escolha, "1") == 0){
            top_brasil(top);
        }
    }
    return 0;
}

