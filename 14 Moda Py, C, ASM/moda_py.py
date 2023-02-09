import ctypes
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

# nasm -f elf64 moda_asm.asm -o moda_asm.o
# gcc -shared moda_asm.o moda_c.c -o lib_moda.so
# python3 moda_py.py

def moda_py (vector,T):

	cont_max = 0
	for n in range(T):
		cont=0
		for m in range(T):
			if(vector[m]==vector[n]):
				cont=cont+1
		if (cont>cont_max):
			cont_max=cont
			valor_max=vector[n]
	return valor_max
    
if __name__ == '__main__':
    # arreglo_prueba_list = [1.5,1.5,1.5,1.5,1.5,1.5,34,5,5,5,3,3,3,2,2]
    # arreglo_prueba = np.array(arreglo_prueba_list, dtype = np.float32)
    
    lib = ctypes.CDLL('./lib_moda.so')
    lib.moda_c.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), ctypes.c_int]
    lib.moda_c.restype = ctypes.c_float

    lib.moda_asm.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), ctypes.c_int]
    lib.moda_asm.restype = ctypes.c_float
    L = [32,64,128,256]
    list_py_t = []
    list_c_t = []
    list_asm_t = []

    for N in (L):
        arreglo_prueba = np.random.rand(N,1).astype(np.float32)
        print(type(arreglo_prueba))
        list_py = []
        list_c = []
        list_asm =[]
        it = 5
        for i in range(it):
            tic = time.time()
            moda_py(arreglo_prueba,N)
            toc = time.time()
            list_py.append(1e6*(toc-tic))

            tic = time.time()
            lib.moda_c(arreglo_prueba,N)
            toc = time.time()
            list_c.append(1e6*(toc-tic))

            tic = time.time()
            lib.moda_asm(arreglo_prueba,N)
            toc = time.time()
            list_asm.append(1e6*(toc-tic))
        list_py_t.append(statistics.median(list_py))
        list_c_t.append(statistics.median(list_c))
        list_asm_t.append(statistics.median(list_asm))
    
    # plt.plot(L,list_py_t,'r')
    plt.plot(L,list_c_t,'g')
    plt.plot(L,list_asm_t,'b')
    plt.savefig('time_test2.png', dpi = 400)
    # plt.plot(list_py,'r')
    # plt.plot(list_c,'g')
    # plt.plot(list_asm,'b')
    # plt.savefig('test2.png')

    print(statistics.median(list_py))
    print(statistics.median(list_c))
    print(statistics.median(list_asm))


    # print(statistics.mode(arreglo_prueba))
    # print(moda_py(arreglo_prueba,len(arreglo_prueba)))
    # print(lib.moda_c(arreglo_prueba,len(arreglo_prueba)))
    # print(lib.moda_asm(arreglo_prueba,len(arreglo_prueba)))