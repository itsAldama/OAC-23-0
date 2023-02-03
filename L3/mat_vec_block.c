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
