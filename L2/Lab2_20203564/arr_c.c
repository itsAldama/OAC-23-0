void func_array_c(int *arreglo_original, int cant, char *arreglo_salida){
    for(int i=0; i<cant; i++){
        if(arreglo_original[i]%2==0){
            arreglo_salida[i]='0'-48;
        }
        else{
            arreglo_salida[i]='1'-48;
        }
    }
}
