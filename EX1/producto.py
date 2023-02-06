import ctypes
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

def calcular_producto_PY(numeros, n, comparador) -> int:
    mayores = 0
    menores = 0
    for i in range(n):
        if numeros[i] > comparador:
            mayores += 1
        elif numeros[i] < comparador:
            menores += 1
    return mayores * menores

if __name__ == "__main__":
    tamaño_arreglo = [128, 256, 512, 1024, 2048]

    iteraciones = 5
    comparador = np.double(0.5)

    lib_producto = ctypes.CDLL('./lib_producto.so')

    lib_producto.calcular_producto_C.argtypes = [np.ctypeslib.ndpointer(dtype = np.float64), ctypes.c_int, ctypes.c_double]
    lib_producto.calcular_producto_C.restype = ctypes.c_int

    lib_producto.calcular_producto_ASM.argtypes = [np.ctypeslib.ndpointer(dtype = np.float64), ctypes.c_int, ctypes.c_double]
    lib_producto.calcular_producto_ASM.restype = ctypes.c_int

    size = len(tamaño_arreglo)
    arr_py = np.zeros(size,dtype=np.float64)
    arr_c = np.zeros(size,dtype=np.float64)
    arr_asm = np.zeros(size,dtype=np.float64)
    j = 0

    for n in tamaño_arreglo:
        numeros = np.random.rand(n).astype(np.float64)

        tiempo_PY = []
        tiempo_C = []
        tiempo_ASM = []

        for i in range(iteraciones):

            tic1 = time.time()
            prod_PY = calcular_producto_PY(numeros, n, comparador)
            toc1 = time.time()
            print(prod_PY)
            tiempo_PY.append(1e6*(toc1-tic1))

            tic2 = time.time()
            prod_C = lib_producto.calcular_producto_C(numeros, n, comparador)
            toc2 = time.time()
            print(prod_C)
            tiempo_C.append(1e6*(toc2-tic2))

            tic3 = time.time()
            prod_ASM = lib_producto.calcular_producto_ASM(numeros, n, comparador)
            toc3 = time.time()
            print(prod_ASM)
            tiempo_ASM.append(1e6*(toc3-tic3))
            print()

        arr_py[j] = statistics.mean(tiempo_PY)
        arr_c[j] = statistics.mean(tiempo_C)
        arr_asm[j] = statistics.mean(tiempo_ASM)
        j += 1

    plt.plot(tamaño_arreglo, arr_py/arr_c, label = 'SpeedUp Python/C', color = 'blue', marker = 'o')
    plt.plot(tamaño_arreglo, arr_py/arr_asm, label = 'SpeedUp Python/ASM', color = 'red', marker = 'o')
    plt.xlabel('Tamaño del arreglo')
    plt.ylabel('Speedup')
    plt.legend()
    plt.savefig('producto.png')