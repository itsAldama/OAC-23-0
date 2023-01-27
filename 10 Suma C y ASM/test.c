#include <stdio.h>
#include <stdlib.h>
extern char suma(char a, char b);

int main(){
    char a = 5;
    char b = 6;
    char c, c_asm;
    c = a + b;
    printf ("C: %d\n", c);

    c_asm = suma(a, b);
    printf("asm: %d\n", c_asm);
}