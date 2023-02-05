import ctypes
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

def calcular_producto_cantidad_mayores_menores_05_PY(numeros, n, comparador) -> int:
    cantidad_mayores_05 = 0
    cantidad_menores_05 = 0
    for i in range(n):
        if numeros[i] > comparador:
            cantidad_mayores_05 += 1
        elif numeros[i] < comparador:
            cantidad_menores_05 += 1
    return cantidad_mayores_05 * cantidad_menores_05

if __name__ == "__main__":
    tamaño_arreglo = [128, 256, 512, 1024, 2048]

    iteraciones = 5
    comparador = np.double(0.5)

    lib_producto = ctypes.CDLL('./lib_producto.so')

    lib_producto.calcular_producto_cantidad_mayores_menores_05_C.argtypes = [np.ctypeslib.ndpointer(dtype = np.float64), ctypes.c_int, ctypes.c_double]
    lib_producto.calcular_producto_cantidad_mayores_menores_05_C.restype = ctypes.c_int

    lib_producto.calcular_producto_cantidad_mayores_menores_05_ASM.argtypes = [np.ctypeslib.ndpointer(dtype = np.float64), ctypes.c_int, ctypes.c_double]
    lib_producto.calcular_producto_cantidad_mayores_menores_05_ASM.restype = ctypes.c_int

    lista_mediana_tiempo_PY = []
    lista_mediana_tiempo_C = []
    lista_mediana_tiempo_ASM = []

    for n in tamaño_arreglo:
        numeros = np.random.rand(n).astype(np.float64)

        lista_tiempo_PY = []
        lista_tiempo_C = []
        lista_tiempo_ASM = []

        for i in range(iteraciones):

            tic1 = time.time()
            prod_cantidad_mayores_menores_05_PY = calcular_producto_cantidad_mayores_menores_05_PY(numeros, n, comparador)
            toc1 = time.time()
            lista_tiempo_PY.append(1e6*(toc1-tic1))

            tic2 = time.time()
            prod_cantidad_mayores_menores_05_C = lib_producto.calcular_producto_cantidad_mayores_menores_05_C(numeros, n, comparador)
            toc2 = time.time()
            lista_tiempo_C.append(1e6*(toc2-tic2))

            tic3 = time.time()
            prod_cantidad_mayores_menores_05_ASM = lib_producto.calcular_producto_cantidad_mayores_menores_05_ASM(numeros, n, comparador)
            toc3 = time.time()
            lista_tiempo_ASM.append(1e6*(toc3-tic3))
        
        lista_mediana_tiempo_PY.append(statistics.median(lista_tiempo_PY))
        lista_mediana_tiempo_C.append(statistics.median(lista_tiempo_C))
        lista_mediana_tiempo_ASM.append(statistics.median(lista_tiempo_ASM))

        print(type(numeros))
    
    plt.plot(tamaño_arreglo, lista_mediana_tiempo_PY, label = 'Python', color = 'blue', marker = 'o')
    plt.plot(tamaño_arreglo, lista_mediana_tiempo_C, label = 'C', color = 'red', marker = 'o')
    plt.plot(tamaño_arreglo, lista_mediana_tiempo_ASM, label = 'ASM', color = 'green', marker = 'o')
    plt.xlabel('Tamaño del arreglo')
    plt.ylabel('Tiempo de ejecución (us)')
    plt.legend()
    plt.savefig('producto.png')