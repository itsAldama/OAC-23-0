import numpy as np
import ctypes
import time
import statistics
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    lib = ctypes.CDLL('./lib.so')
    lib.mat_vec.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32),
                            np.ctypeslib.ndpointer(dtype=np.int32),
                            np.ctypeslib.ndpointer(dtype=np.int32),
                            ctypes.c_int]

    lib.mat_vec_block.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32),
                                np.ctypeslib.ndpointer(dtype=np.int32),
                                np.ctypeslib.ndpointer(dtype=np.int32),
                                ctypes.c_int, ctypes.c_int]

    max_val_mas_1 = 10
    # blocks = [2,4,8,16]
    blocks =  2**np.arange(1,5)

    iteraciones = 15
    t1_total = []
    t2_total = []
    t3_total = []
    #Cambiar el valor de 5 y 8 según requerimiento del problema. Para este ejemplo, ns = [2^{5}, 2^{6}, 2^{7}, 2^{8}]
    ns = 2**np.arange(5,9)

    for block in blocks:

        for N in ns:
        
            A = np.random.randint(max_val_mas_1-1,size =(N,N),dtype = np.int32)
            B = np.random.randint(max_val_mas_1-1,size =(N,N),dtype = np.int32)
            
            A_array = A.flatten()
            B_array = B.flatten()

            C_mat_vec = np.zeros_like(A_array, dtype=np.int32)
            C_mat_vec_blocking = np.zeros_like(A_array, dtype=np.int32)

            C_mat_vec_array = C_mat_vec.flatten()
            C_mat_vec_blocking = C_mat_vec_blocking.flatten()
            
            t1 = []
            t2 = []
            t3 = []


            # Se realiza el cálculo de la mediana de los tiempos de ejecución de cada función
            for it in range(iteraciones):
                
                # Se calcula el tiempo de ejecución de cada función

                tic1 = time.time()
                lib.mat_vec(A_array,B_array,C_mat_vec_array, N)
                toc1 = time.time()

                tic2 = time.time()
                lib.mat_vec_block(A_array,B_array,C_mat_vec_blocking, N, block)
                toc2 = time.time()

                tic3 = time.time()
                np.dot(A,B)
                toc3 = time.time()

                t1.append(toc1-tic1)
                t2.append(toc2-tic2)
                t3.append(toc3-tic3)
            t1_total.append(statistics.median(t1))
            t2_total.append(statistics.median(t2))
            t3_total.append(statistics.median(t3))

        plt.plot(list(ns),t1_total)
        plt.plot(list(ns),t2_total)
        plt.plot(list(ns),t3_total)
        plt.grid()
        plt.legend(['Matriz_vector','Matriz_vector_blocking', 'Matriz_vector_dot'])
        plt.savefig(('Tiempo_ejecucion_block_'+str(block)+'.png'), dpi = 400)
        plt.close()

        t1_total.clear()
        t2_total.clear()
        t3_total.clear()