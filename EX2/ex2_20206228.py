import time
from math import floor, sqrt, ceil
from multiprocessing import Pool, Queue, Process

n = 2345678911111111
    
def verificar_es_primo(numero):

    es_primo = True

    for i in range(2, floor(sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            return es_primo
    
    return es_primo

def verificar_primo(nums_evaluar: list):

    for i in nums_evaluar:
        if n % i == 0:
            return False
    return True

def dividir_numeros_inicio(n, jump):
    for i in range(2, n, jump):
        yield list(range(i, i+jump))

def dividir_numeros_fin(n, jump):
    for i in range(2, n, jump):
        yield i+jump

def verificar_es_primo_multi(numero):

    ultimo = floor(sqrt(numero)) + 1
    
    num_procc = 24

    # p = Pool(processes=num_procc)

    # // redondea hacia abajo
    jump = ceil((ultimo-2)/num_procc)
    
    chunks = list(dividir_numeros_inicio(ultimo, jump))
    # final = list(dividir_numeros_fin(n, jump))
    print("chunks")
    # print(chunks)
    with Pool(processes=num_procc) as pool:
        results = pool.map(verificar_primo, chunks)
    
    if False in results:
        return False
    else:
        return True

    # p1 = Process(target=verificar_primo, args=(2, ultimo//2, numero, ))
    # p2 = Process(target=verificar_primo, args=(ultimo//2, ultimo, numero, ))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

if __name__ == "__main__":
    # n = 2345678911111111
    # n = 2382847902741

    # tic = time.perf_counter()
    # es_primo_sin = verificar_es_primo(n)
    # toc = time.perf_counter()
    # sin_multiprocess_time = toc-tic

    # print()
    # print("Tiempo de ejecución sin multiprocessing:", sin_multiprocess_time)

    tic = time.perf_counter()
    es_primo_con = verificar_es_primo_multi(n)
    toc = time.perf_counter()
    con_multiprocess_time = toc-tic
    print("Es primo?", es_primo_con)
    print("Tiempo de ejecución con multiprocessing:", con_multiprocess_time, end="\n\n")
    
    # assert(es_primo_sin==es_primo_con)
    # print("Prueba assert pasada correctamente los resultados son iguales", end="\n\n")
    # print(f"Speed Up sin_multiprocess_time/con_multiprocess_time: {sin_multiprocess_time/con_multiprocess_time: 0.2f}", end="\n\n")