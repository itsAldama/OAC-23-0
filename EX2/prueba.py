import numpy as np
from itertools import repeat

M = 4
N = 5

mat_M = np.random.randint(100, size=(M, N))
vector_A = np.random.randint(100, size=(N))
args = zip(mat_M, repeat(vector_A))

print(mat_M)
print()
print(vector_A)
print()

for arg in args:
    print(arg)

def generator(n):
    for i in range(n):
        yield(int(i**2))

if __name__ == "__main__":
    n = 20
    gen = generator(n)
    print(gen)
    
    # solo puedo usar una vez el generator,  luego se queda vacío
    for n in gen:
        print(n, hex(id(n)))

    # a = list(gen)
    # print()
    # for i in a:
    #     print(i, hex(id(i)))
    
    print()
    print("#######")
    gen = generator(20)
    gen = list(gen)
    print(gen)
    print(type(gen[0]))
    for n in gen:
        print(n, hex(id(n)))