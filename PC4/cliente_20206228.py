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

    numero_envios = 7
    for i in range(numero_envios):
        if i == 0:
            msg = input("Escribir su nombre: ")
        elif i == 1:
            msg = "error"
            while msg != "equipos":
                msg = input("Escribir 'equipos' para generar las listas de jugadores: ")
        elif i == 2:
            msg = "error"
            while msg != "fase de grupos asincrono":
                msg = input("Escribir 'fase de grupos asincrono': ")
        elif i == 3:
            msg = "error"
            while msg != "fase de grupos sincrono":
                msg = input("Escribir 'fase de grupos sincrono': ")
        elif i == 4:
            msg = "error"
            while msg != "eliminatorias asincrono":
                msg = input("Escribir 'eliminatorias asincrono': ")
        elif i == 5:
            msg = "error"
            while msg != "eliminatorias sincrono":
                msg = input("Escribir 'eliminatorias sincrono': ")
        else:
            msg = "error"
            while msg != "reporte":
                msg = input("Escribir 'reporte' para ver las listas obtenidas y tiempos de ejecucion: ")
        msg = msg.encode("utf-8")

        sock.sendall(msg)
        data = sock.recv(SOCK_BUFFER)

        print(f"Recibido: {data.decode('utf-8')}\n")
    
    sock.sendall("quit".encode("utf-8"))
    sock.close()
