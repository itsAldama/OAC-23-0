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
