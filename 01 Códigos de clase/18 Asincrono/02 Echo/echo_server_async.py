import asyncio
import socket

async def handle_client(conn, client_address):
    print(f"Conexión desde {client_address}")
    loop = asyncio.get_event_loop()
    request = None
    while request != "quit":
        request = (await loop.sock_recv(conn, 1024)).decode("utf-8")
        print(f"Recibido: {request}")
        await loop.sock_sendall(conn, request.encode("utf-8"))
    print("Cerrando conexión con el cliente")
    conn.close()


async def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)

    loop = asyncio.get_event_loop()

    while True:
        conn, client_address = await loop.sock_accept(sock)
        loop.create_task(handle_client(conn, client_address))


if __name__ == '__main__':
    asyncio.run(run_server())