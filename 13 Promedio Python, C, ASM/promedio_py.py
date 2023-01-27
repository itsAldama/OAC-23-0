import ctypes
import numpy as np 
import statistics

if __name__ == '__main__':
    # nasm -f elf64 promedio_asm.asm -o promedio_asm.o
    # gcc -shared promedio_asm.o lib_promedio_c.c -o lib_promedio.so
    # python3 promedio_py.py

    # s2
    
    size = 10
    x = np.random.randint(2,100,size,dtype = np.int32)

    lib = ctypes.CDLL('./lib_promedio.so')
    lib.promedio_c.argtypes= [np.ctypeslib.ndpointer(dtype = np.int32), ctypes.c_int]
    lib.promedio_c.restype = ctypes.c_int

    lib.promedio_asm.argtypes= [np.ctypeslib.ndpointer(dtype = np.int32), ctypes.c_int]
    lib.promedio_asm.restype = ctypes.c_int

    print(statistics.mean(x))
    print(lib.promedio_c(x,size))
    print(lib.promedio_asm(x,size))