from threading import Thread
import socket

SOCK_BUFFER = 1024
num_clientes = 0

def handle_client(connection, client_address):
    global num_clientes
    num_clientes += 1
    print(f"Clientes conectados: {num_clientes}")

    try:
        print(f"Conexión desde {client_address}")
        while True:
            data = connection.recv(SOCK_BUFFER)
            print(f"Recibido: {data.decode('utf-8')}")
            if data:
                print(f"Enviando: {data.decode('utf-8')}\n")
                connection.sendall(data)
            else:
                print("No hay más datos")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cerrando la conexión con el cliente")
        connection.close()
        num_clientes -= 1
        print(f"Clientes conectados: {num_clientes}")

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexión ...")

        connection, client_address = sock.accept()

        client_thread = Thread(target=handle_client, args=(connection, client_address))
        client_thread.start()
