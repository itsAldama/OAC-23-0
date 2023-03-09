from threading import Thread
import time

CUENTA = 100

def cuenta(n):
    while n > 0:
        print(n)
        n -= 1

if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(CUENTA//2,))
    t2 = Thread(target=cuenta, args=(CUENTA//2,))
    t1.start()
    t2.start()
    # Espera a que los hilos terminen su ejecución
    t1.join()
    t2.join()

    fin = time.perf_counter()
    print(f"Tiempo de cuenta descendente multihilo: {fin - inicio} segundos")