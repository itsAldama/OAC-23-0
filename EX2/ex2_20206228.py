import time
from math import floor, sqrt, ceil
from multiprocessing import Pool
import matplotlib.pyplot as plt
from statistics import median

# numero a verificar
n = 2_345_678_911_111_111

def grafico_tiempo_vs_procesos():
    procesos = [2,4,8,16]
    procesos_tiempo = []

    for proceso in procesos:
        tiempos = []

        # realizamos 5 pruebas para sacar la mediana y tener una respuesta más exacta
        for i in range(5):
            inicio = time.perf_counter()
            es_primo = verificar_es_primo_multi(n, proceso)
            fin = time.perf_counter()
            tiempos.append(fin-inicio)
        
        tiempo = median(tiempos)
        procesos_tiempo.append(tiempo)
    # print(procesos)
    # print(procesos_tiempo)
    plt.plot(procesos, procesos_tiempo, label = 'Procesos vs Tiempo', color = 'red', marker = 'o')
    plt.xlabel('Números de Procesos')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.savefig('procesos_tiempo.png')

    # c) Aumentar el número de procesos no hace que el tiempo disminuya necesariamente,
    #   solo hasta con 4 puede ser que disminuya, pero en el resto incrementa considerablemente
    #   esto se debe a la cantidad de cores que tiene nuestra pc, si le mandamos más procesos que la cantidad
    #   core que tiene, un solo core estará ejecutando varios procesos que ocupan memoria y lo hará más lento.

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

# usamos el generador para no ocupar mucha memoria
def dividir_numeros_inicio(n, jump):
    for i in range(2, n, jump):
        yield i

def dividir_numeros_fin(n, jump):
    for i in range(2, n, jump):
        yield i+jump

def verificar_es_primo_multi(numero, num_procesos=2):
    if numero<=3:
        return True

    ultimo = floor(sqrt(numero)) + 1
    
    # nos va a ayudar a tener divisiones de numeros para tener el numero de procesos pedido en num_procc
    jump = ceil((ultimo-2)/num_procesos)

    # hacemos 2 listas con los numeros de inicio y de final
    inicio = list(dividir_numeros_inicio(ultimo, jump))
    final = list(dividir_numeros_fin(ultimo, jump))

    # zippeamos el primero del inicio y del final, y así sucesivamente
    chunks = zip(inicio, final)
    
    with Pool(processes=num_procesos) as pool:
        # mandamos a la función el inicio y final del rango de numeros que va a verificar si alguno es divisible entre el numero
        results = pool.starmap(verificar_es_primo_chunk, chunks)
    
    # si algunos de nuestros procesos encontró un divisor para el numero,
    # entonces el numero no es primo
    if False in results:
        return False
    else:
        return True

if __name__ == "__main__":

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
    print("Tiempo de ejecución con multiprocessing 2 procesos:", con_multiprocess_time, end="\n\n")
    
    assert(es_primo_sinc==es_primo_con)
    print("PRUEBA ASSERT PASADA CORRECTAMENTE, LOS RESULTADOS SON IGUALES")
    print("EL NUMERO ES PRIMO?", es_primo_con, end="\n\n")
    print(f"Speed Up sin_multiprocess_time/con_multiprocess_time: {sin_multiprocess_time/con_multiprocess_time: 0.2f}", end="\n\n")

    # descomentar para generar de nuevo el gráfico
    # grafico_tiempo_vs_procesos()