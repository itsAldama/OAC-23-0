extern float moda_asm(float *vector, int L);

float moda_c (float *vector, int L)
{
	int cont_max=0;
	int cont;
	float valor_max;

	for(int n=0;n<L;n++)
	{
		cont=0;
		for(int m=0;m<L;m++)
		{
			if (vector[m] == vector[n])
			{
				cont++;
			}
		}
	if (cont>cont_max)
	{
		cont_max=cont;
		valor_max=vector[n];
	}
	}
	return valor_max;
}