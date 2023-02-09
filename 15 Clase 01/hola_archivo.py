# xkcd

def fun(a: int, b: int) -> int:
    return a + b

print("Fuera")

if __name__ == '__main__':
    # Cuando la llamo como un archivo desde otro código, no se muestra
    print("Dentro")
    print(fun(1,2))