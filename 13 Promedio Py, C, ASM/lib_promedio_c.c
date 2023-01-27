extern int promedio_asm(int *vector, int N);

int promedio_c(int *vector, int N)
{
    int suma=0;
    for (int i=0;i<N;i++)
    {
        suma = suma+vector[i];
    }
    return suma/N;
}