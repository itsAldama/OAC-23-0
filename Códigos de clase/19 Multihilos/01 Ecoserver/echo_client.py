import socket
import time

MSG_NUM = 10
SOCK_BUFFER = 4
SLEEP_TIME = 1

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.1.5", 5000)

    print(f"Conectando a servidor -> {server_address[0]} en el puerto -> {server_address[1]}")

    sock.connect(server_address)

    try:
        for i in range(MSG_NUM):
            msg = f"Este es el mensaje de prueba {i+1}"
            msg = msg.encode("utf-8")
            sock.sendall(msg)

            amnt_recvd = 0
            amnt_expected = len(msg)
            msg_rx = ""

            while amnt_recvd < amnt_expected:
                data = sock.recv(SOCK_BUFFER)
                amnt_recvd += len(data)
                msg_rx += data.decode("utf-8")

            print(f"Recibido: {msg_rx}")
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Usuario canceló la ejecución del programa")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cerrando conexión")
        sock.close()