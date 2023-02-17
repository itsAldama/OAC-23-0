import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    # Creo el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('0.0.0.0', 5000)
    print(f"Iniciando servido en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(2)

    while True:
        print("Esperando una conexión")

        connection, client_address = sock.accept()

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