import time
from math import floor, sqrt, ceil
from multiprocessing import Pool, Queue, Process

n = 2345678911111111
# n = 2000

def verificar_es_primo_sinc(numero):

    for i in range(2, floor(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    
    return True

def verificar_es_primo_chunk(ini, fin):

    for i in range(ini, fin):
        if n % i == 0:
            return False
    return True

def dividir_numeros_inicio(n, jump):
    for i in range(2, n, jump):
        yield i

def dividir_numeros_fin(n, jump):
    for i in range(2, n, jump):
        yield i+jump

def verificar_es_primo_multi(numero):

    ultimo = floor(sqrt(numero)) + 1
    
    num_procc = 8

    jump = ceil((ultimo-2)/num_procc)

    inicio = list(dividir_numeros_inicio(ultimo, jump))
    final = list(dividir_numeros_fin(ultimo, jump))

    chunks = zip(inicio, final)
    
    print(inicio)
    print(final)
    with Pool(processes=num_procc) as pool:
        results = pool.starmap(verificar_es_primo_chunk, chunks)
    
    if False in results:
        return False
    else:
        return True

if __name__ == "__main__":
    # n = 2345678911111111
    # n = 2382847902741

    tic = time.perf_counter()
    es_primo_sinc = verificar_es_primo_sinc(n)
    toc = time.perf_counter()
    sin_multiprocess_time = toc-tic

    print()
    print("Tiempo de ejecución sin multiprocessing:", sin_multiprocess_time)

    tic = time.perf_counter()
    es_primo_con = verificar_es_primo_multi(n)
    toc = time.perf_counter()
    con_multiprocess_time = toc-tic
    print("Es primo?", es_primo_con)
    print("Tiempo de ejecución con multiprocessing:", con_multiprocess_time, end="\n\n")
    
    assert(es_primo_sinc==es_primo_con)
    print("PRUEBA ASSERT PASADA CORRECTAMENTE, LOS RESULTADOS SON IGUALES", end="\n\n")
    print(f"Speed Up sin_multiprocess_time/con_multiprocess_time: {sin_multiprocess_time/con_multiprocess_time: 0.2f}", end="\n\n")