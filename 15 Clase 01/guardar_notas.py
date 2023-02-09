import random
import time

if __name__ == "__main__":  
    inicio_total = time.perf_counter()
    codigo_base = 20230000
    contenido = ""
    for i in range(40):
        pa = [random.randint(0, 20) for _ in range(4)]
        pb = [random.randint(0, 20) for _ in range(5)]
        e1 = random.randint(0, 20)
        e2 = random.randint(0, 20)
        linea = f"{codigo_base + i}, {pa[1]}, {pa[2]}, {pa[3]}, {pb[0]}, {pb[1]}, {pb[2]}, {pb[3]}, {pb[4]}, {e1}, {e2}\n"
        contenido += linea

    with open("notas.csv", "w+") as archivo:
        archivo.write(contenido)

    fin_total = time.perf_counter()