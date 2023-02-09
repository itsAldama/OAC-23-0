import hola_archivo
import time

if __name__ == "__main__":
    # eficiencia: tiempo de ejecución en el curso
    i = time.perf_counter()
    print(hola_archivo.fun(1,3))
    f = time.perf_counter()

    print(f"Tiempo de ejecucion: {(f-i)} segundos")