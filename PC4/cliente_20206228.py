import socket
import time
import random

SOCK_BUFFER = 10000000

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("192.168.1.5", 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    client_id = random.randint(0, 1000)

    for i in range(10):
        msg = input("Mensaje: ")
        msg = msg.encode("utf-8")

        inicio_tx= time.perf_counter()
        sock.sendall(msg)
        fin_tx = time.perf_counter()
        print(f"Tiempo de transmisión: {fin_tx - inicio_tx:0.4f} segundos")

        amnt_recvd = 0
        total_data = b""

        # inicio_rx = time.perf_counter()
        # while True:
        #     print(data)
        #     if not data:
        #         break
        #     total_data += data

        # fin_rx = time.perf_counter()

        # print(f"Tiempo de recepción: {fin_rx - inicio_rx:0.4f} segundos")
        data = sock.recv(SOCK_BUFFER)

        print(f"Recibido: {data.decode('utf-8')}")
        # time.sleep(1)
    
    # sock.sendall("quit".encode("utf-8"))
    sock.close()
