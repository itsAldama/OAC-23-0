// gcc --shared producto_ASM.o lib_producto.c -o lib_producto.so 

extern int calcular_producto_cantidad_mayores_menores_05_ASM(double *numeros, int n, double comparador);

int calcular_producto_cantidad_mayores_menores_05_C(double *numeros, int n, 
                                                    double comparador){
    int mayores = 0;
    int menores = 0;
    for(int i = 0; i < n; i++) {
        if(numeros[i] > comparador) {
            mayores++;
        } else if(numeros[i] < comparador) {
            menores++;
        }
    }
    return mayores * menores;
}
