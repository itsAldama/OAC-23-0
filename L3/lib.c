// Para generar el archivo .so, debe escribir en el terminal lo siguiente:
// gcc -shared lib.c -o lib.so

void mat_vec(int *A, int *B, int *C, int N) 
{
    int tmp = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            C[i*N+j]=0;
            for(int k = 0;k<N;k++){
                C[i*N+j] += A[i*N + k]*B[k*N+j];
            }
        }
    }   
}

void mat_vec_block(int *A, int *B, int *C, int N, int block)
{
    int i,j,k,kk,jj;
    int sum;
    int en = block*(N/block);

    for (kk = 0; kk < en; kk += block) {
        for (jj = 0; jj < en; jj += block) {
            for(i = 0; i < N; i++){
                for (j = jj; j < jj + block; j++){
                    sum = C[i*N+j];
                    for (k = kk; k < kk + block; k++)
                    {
                        sum+= A[i*N+k]*B[k*N+j];
                    }
                    C[i*N+j]= sum;
                }
            }
        }
    }   
}
