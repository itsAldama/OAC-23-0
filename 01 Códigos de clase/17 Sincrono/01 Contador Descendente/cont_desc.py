import time

CUENTA = 200_000_000

def cuenta(n):
    while n > 0:
        print(n)
        n -= 1

if __name__ == '__main__':
    inicio = time.perf_counter()
    cuenta(CUENTA)
    fin = time.perf_counter()
    print(f"Tiempo de cuenta descendente síncrona: {fin - inicio} segundos")