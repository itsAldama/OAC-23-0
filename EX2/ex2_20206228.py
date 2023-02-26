import time
from math import floor, sqrt
from multiprocessing import Pool, Queue, Process
    
def verificar_es_primo(numero):

    es_primo = True

    for i in range(2, floor(sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            return es_primo
    
    return es_primo

def verificar_primo(inicio, fin, numero, q):

    for i in range(inicio, fin):
        if numero % i == 0:
            q.put(False)
            return
    
    q.put(True)

def verificar_es_primo_multi(numero):
    q = Queue()

    ultimo = floor(sqrt(numero)) + 1
    p1 = Process(target=verificar_primo, args=(2, ultimo//2, numero, q, ))
    p2 = Process(target=verificar_primo, args=(ultimo//2, ultimo, numero, q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    return q.get() and q.get()

if __name__ == "__main__":
    n = 2345678911111111
    # n = 2382847902741
    # n = 20

    tic = time.perf_counter()
    es_primo_sin = verificar_es_primo(n)
    toc = time.perf_counter()
    sin_multiprocess_time = toc-tic

    print()
    print("Tiempo de ejecución sin multiprocessing:", sin_multiprocess_time)

    tic = time.perf_counter()
    es_primo_con = verificar_es_primo_multi(n)
    toc = time.perf_counter()
    con_multiprocess_time = toc-tic
    print("Tiempo de ejecución con multiprocessing:", con_multiprocess_time, end="\n\n")
    
    assert(es_primo_sin==es_primo_con)
    print("Prueba assert pasada correctamente los resultados son iguales", end="\n\n")
    print(f"Speed Up sin_multiprocess_time/con_multiprocess_time: {sin_multiprocess_time/con_multiprocess_time: 0.2f}", end="\n\n")