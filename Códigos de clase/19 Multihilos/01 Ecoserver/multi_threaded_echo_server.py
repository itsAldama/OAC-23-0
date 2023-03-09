import socket
from threading import Thread

SOCK_BUFFER = 1024
num_clientes = 0

# 1 hilo para cada conexión

def client_handler(conn, client_address):
    global num_cliente
    try:
        print(f"Conexión desde {client_address[0]}")

        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data} de {client_address}")
                conn.sendall(data)
            else:
                print("No hay más datos")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cerrando conexión con el cliente")
        num_clientes -= 1
        conn.close()

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexión...")

        conn, client_address = sock.accept()

        #hilo es una unidad de procesamiento

        client_thread = Thread(target=client_handler, args=(conn, client_address))
        client_thread.start()