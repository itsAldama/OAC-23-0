import concurrent.futures
from threading import Lock
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self.lock = Lock()
    
    def update(self, name):
        print(f"Thread {name}: iniciando actualizacion")
        print(f"Thread {name}: a punto de adquirir el candado")
        with self.lock:
            print(f"Thread {name}: candado adquirido")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name}: a punto de liberar el candado")
        print(f"Thread {name}: candado liberado")
        print(f"Thread {name}: actualizacion completa")


if __name__ == '__main__':
    workers = 10

    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        list(map(lambda x: executor.submit(db.update, x), range(workers)))

    print((map(lambda x: x**2, range(10))))
    
    print(f"Valor final de la base de datos: {db.value}")