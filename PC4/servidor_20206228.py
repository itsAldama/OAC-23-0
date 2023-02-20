import statistics
import csv
import random
import socket
import time
import asyncio

# Diccionario que contendrá los equipos y cada equipo una lista de minutos jugados por sus jugadores
equipos = {}
datos_ordenados = []

def leer_archivo():
    global datos_ordenados
    teams = []
    with open("datos.csv", "r") as file:
        reader = csv.DictReader(file)
        for team in reader:
            teams.append(team)

    # Ordenamos la lista de dictionarios primero por el valor de la llave 'Team' y luego por el valor de la llave 'MIN' que primero pasamos a float
    # Esto es para que los equipos esten ordenados alfabeticamente y luego por minutos jugados
    datos_ordenados = sorted(teams, key=lambda k:[k['Team'], float(k['MIN'])], reverse=True)
    
def equipos_max_minutos(datos_ordenados):
    cnt = 0
    # Recorremos la lista de dictionarios ordenada
    for _dict in datos_ordenados:
        cnt += 1
        # Si el contador es mayor a 5, significa que ya se han agregado 5 jugadores de un equipo
        if (cnt>5):
            # Si el equipo actual es diferente al equipo anterior, agregamos el nuevo equipo
            if _dict['Team'] != prev:
                cnt = 1
        # Si el contador es menor o igual a 5, significa que se pueden agregar mas jugadores de un equipo
        if(cnt<=5):
            # Agregamos la primera vez al equipo en el diccionario
            if cnt == 1:
                equipos[_dict['Team']] = []
            else:
                # Puede ser que un equipo aparezca menos de 5 veces, por lo que si el equipo actual es 
                # diferente al equipo anterior agregamos el nuevo equipo al diccionario
                if _dict['Team'] != prev:
                    equipos[_dict['Team']] = []
                    cnt = 1
            # Agregamos el minuto del jugador al equipo
            equipos[_dict['Team']].append(_dict['Player'])
        prev = _dict['Team']

    # b) Equipos y sus listas globales de jugadores con más minutos jugados
    for equipo,min in equipos.items():
        print(f'{equipo:4} : {min}')
    return equipos

# c) Función que retorna el equipo ganador de forma aleatoria para la fase de eliminatorias
def partido(equipo1, equipo2):
    if random.randint(0,1) == 0:
        return equipo1
    else:
        return equipo2

def obtener_puntaje_promedio(datos_ordenados,equipo):
    cnt = 0
    pnts = 0
    for _dict in datos_ordenados:
        if _dict['Team'] == equipo:
            cnt += 1
            pnts += float(_dict['PTS'])
    return pnts/cnt


def partido_puntos(datos_ordenados,equipo_i, equipo_j):
    pnts_i = obtener_puntaje_promedio(datos_ordenados,equipo_i)
    pnts_j = obtener_puntaje_promedio(datos_ordenados,equipo_j)
    if pnts_i > pnts_j:
        return (equipo_i,pnts_i)
    else:
        return (equipo_j,pnts_j)

def grupos_sync(participantes, datos_ordenados):
    ganadores_g = {}
    for grupo, equipos in participantes.items():
        ganadores = {}
        for i in range(len(equipos)):
            for j in range(i+1, len(equipos)):
                # ganador = (equipo, puntaje)
                print(f"Partido entre {equipos[i]} vs {equipos[j]}")
                ganador = partido_puntos(datos_ordenados,equipos[i], equipos[j])
                print(f"Ganador: {ganador[0]} con puntaje {ganador[1]}")
                # sumamos los puntos del equipo ganador
                if ganador[0] not in ganadores.keys():
                    ganadores[ganador[0]] = 3
                else:
                    ganadores[ganador[0]] += 3
                time.sleep(0.15)
        ganadores_g[grupo] = ganadores

    print()
    
    ganadores_g_lista = []
    for equipos_puntajes in ganadores_g.values():
        # Ordenamos los equipos por puntaje
        equipos_puntajes = sorted(equipos_puntajes.items(), key=lambda x: x[1], reverse=True)

        # Agregamos los 2 de más puntaje del grupo a la lista de ganadores
        for i in range(2):
            ganadores_g_lista.append(equipos_puntajes[i][0])

    return ganadores_g_lista

def simular_round(restantes, n, tercer_lugar, podio_sync):
    winners = []
    for i in range(0, len(restantes), 2):
        print(f"Partido entre {restantes[i]} vs {restantes[i+1]}")
        if partido(restantes[i], restantes[i+1]) == restantes[i]:
            winners.append(restantes[i])
            print(f"Ganador: {restantes[i]}", end='\n\n')
            if n == 4:
                print(f"El perdedor en semis es {restantes[i+1]}", end='\n\n')
                tercer_lugar.append(restantes[i+1])
            elif n == 2:
                podio_sync[1] = restantes[i+1]
                podio_sync[0] = restantes[i]
        else:
            winners.append(restantes[i+1])
            print(f"Ganador: {restantes[i+1]}", end='\n\n')
            if n == 4:
                print(f"El perdedor en semis es {restantes[i]}", end='\n\n')
                tercer_lugar.append(restantes[i])
            elif n == 2:
                podio_sync[1] = restantes[i]
                podio_sync[0] = restantes[i+1]
    return winners

async def octavos_dif_grupos_async(clasificados, restantes, i, j):
    j *= 4
    if i == 0:
        curr = j
        next = curr+3
    else:
        curr = j+1
        next = curr+1

    print(f"Partido entre {clasificados[curr]} vs {clasificados[next]}")
    ganador = partido(clasificados[curr], clasificados[next])
    print(f"Ganador: {ganador}", end='\n\n')
    restantes.append(ganador)
    time.sleep(0.15)

async def octavos_async(clasificados, restantes, i):
    # Cada 2 grupos se cambiar a los siguientes 2 grupos
    await asyncio.gather(*(octavos_dif_grupos_async(clasificados, restantes, i, j) for j in range(4)))

async def eliminatorias_async(clasificados_async):
    # Partidos de cada etapa en simultaneo con async y una empieza cuando otra termina
    print("FASE DE ELIMINATORIAS", end='\n\n')
    restantes = []

    print(f"************{'OCTAVOS DE FINAL':^30}************", end='\n\n')

    print(clasificados_async)
    await asyncio.gather(*(octavos_async(clasificados_async, restantes, i) for i in range(0, 2)))
    print("Restantes: ", restantes, end='\n\n')

    # Creamos una lista para los 2 equipos que jugaran por el 3er lugar
    tercer_lugar = []
    podio_async = [0,0,0]
    # Simulamos los partidos de los 8vos, 4tos, semifinales y final
    # se irá actualizando la lista de equipos restantes hasta que quede el ganador
    while len(restantes)>1:
        if len(restantes)==8:
            print(f"************{'CUARTOS DE FINAL':^30}************", end='\n\n')
        elif len(restantes)==4:
            print(f"************{'SEFIMIFINALES':^30}************", end='\n\n')
        elif len(restantes)==2:
            print(f"************{'FINAL':^30}************", end='\n\n')
        restantes = simular_round(restantes, len(restantes), tercer_lugar, podio_async)
    print(f"************{'TERCER LUGAR':^30}************", end='\n\n')
    print(f"Partido entre {tercer_lugar[0]} vs {tercer_lugar[1]}")
    podio_async[2] = partido(tercer_lugar[0], tercer_lugar[1])
    print("Ganador: ", podio_async[2], end='\n\n')
    return podio_async

def eliminatorias_sync(clasificados_sync):
    # Enfrentamiento del 1ro del grupo A con el 2do del grupo B y sucesivamente

    print("FASE DE ELIMINATORIAS", end='\n\n')
    print(f"************{'OCTAVOS DE FINAL':^30}************", end='\n\n')
    
    restantes = []
    print(clasificados_sync, end='\n\n')
    for i in range(2):
        for j in range(4):
            j *= 4
            if i == 0:
                curr = j
                next = curr+3
            else:
                curr = j+1
                next = curr+1

            print(f"Partido entre {clasificados_sync[curr]} vs {clasificados_sync[next]}")
            ganador = partido(clasificados_sync[curr], clasificados_sync[next])
            print(f"Ganador: {ganador}", end='\n\n')
            restantes.append(ganador)
            time.sleep(0.15)
    
    # Creamos una lista para los 2 equipos que jugaran por el 3er lugar
    tercer_lugar = []
    podio_sync = [0,0,0]
    # Simulamos los partidos de los 8vos, 4tos, semifinales y final
    # se irá actualizando la lista de equipos restantes hasta que quede el ganador
    while len(restantes)>1:
        if len(restantes)==8:
            print(f"************{'CUARTOS DE FINAL':^30}************", end='\n\n')
        elif len(restantes)==4:
            print(f"************{'SEFIMIFINALES':^30}************", end='\n\n')
        elif len(restantes)==2:
            print(f"************{'FINAL':^30}************", end='\n\n')
        restantes = simular_round(restantes, len(restantes), tercer_lugar, podio_sync)

    print(f"************{'TERCER LUGAR':^30}************", end='\n\n')
    print(f"Partido entre {tercer_lugar[0]} vs {tercer_lugar[1]}")
    podio_sync[2] = partido(tercer_lugar[0], tercer_lugar[1])
    print("Ganador: ", podio_sync[2], end='\n\n')
    return podio_sync

async def enfrentamiento_async(grupo, equipos, ganadores_g, ganadores, i, j):
    print(f"Partido entre {equipos[i]} vs {equipos[j]}")
    ganador = partido_puntos(datos_ordenados,equipos[i], equipos[j])
    print(f"Ganador: {ganador[0]} con puntaje {ganador[1]}")
    # sumamos los puntos del equipo ganador
    if ganador[0] not in ganadores.keys():
        ganadores[ganador[0]] = 3
    else:
        ganadores[ganador[0]] += 3
    time.sleep(0.15)

async def enfrentamientos_async(grupo, equipos, ganadores_g, ganadores, i):
    await asyncio.gather(*(enfrentamiento_async(grupo, equipos, ganadores_g, ganadores, i, j) for j in range(i+1, len(equipos))))

async def partidos_async(grupo, equipos, ganadores_g):
    ganadores = {}

    await asyncio.gather(*(enfrentamientos_async(grupo, equipos, ganadores_g, ganadores, i) for i in range(len(equipos))))
    ganadores_g[grupo] = ganadores

async def grupos_async(participantes, datos_ordenados):
    ganadores_g = {}

    # Partidos de cada grupo en simultaneo con async
    await asyncio.gather(*(partidos_async(grupo, equipos, ganadores_g) for grupo, equipos in participantes.items()))
    print()
    
    ganadores_g_lista = []
    for equipos_puntajes in ganadores_g.values():
        # Ordenamos los equipos por puntaje
        equipos_puntajes = sorted(equipos_puntajes.items(), key=lambda x: x[1], reverse=True)

        # Agregamos los 2 de más puntaje del grupo a la lista de ganadores
        for i in range(2):
            ganadores_g_lista.append(equipos_puntajes[i][0])

    return ganadores_g_lista

if __name__ == "__main__":
    # Equipos participantes en la fase de grupos
    participantes = {'A':['ATL','BOS','BRK','CHA'], 'B':['DAL','DEN','DET','GSW'],
                 'C':['LAC','LAL','MEM','MIA'], 'D':['NOP','NYK','OKC','ORL'],
                 'E':['POR','SAC','SAS','SEA'], 'F':['WAS','CHI','CLE','UTA'],
                 'G':['HOU','IND','MIL','MIN'], 'H':['PHI','PHX','TOR','BOL']}
    
    leer_archivo()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print(f"Inicianndo servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(2)

    while True:
        print("Esperando conexion...")

        connection, cliente_address = sock.accept()

        try:
            print(f"Conexion desde {cliente_address}")
            while True:
                data = connection.recv(1024)
                print(f"Recibido {data.decode('utf-8')}")
                if data:
                    if data.decode('utf-8') == "equipos":
                        # i) Generar listas de jugadores que pertenecen al mismo equipo y
                        #    tengan el valor más alto de minutos jugados
                        equipos = equipos_max_minutos(datos_ordenados)
                        connection.sendall(str(equipos).encode('utf-8'))

                    elif data.decode('utf-8') == "fase de grupos sincrono":
                        # e) Retorna las listas con los 2 primeros lugares de cada grupo
                        clasificados_sync = grupos_sync(participantes, datos_ordenados)
                        connection.sendall(str(clasificados_sync).encode('utf-8'))

                    elif data.decode('utf-8') == "fase de grupos asincrono":
                        # d) Retorna las listas con los 2 primeros lugares de cada grupo
                        clasificados_asinc = asyncio.run(grupos_async(participantes, datos_ordenados))
                        connection.sendall(str(clasificados_asinc).encode('utf-8'))
                        
                    elif data.decode('utf-8') == "eliminatorias sincrono":
                        # g) Retorna la lista con el podio de la fase de eliminatorias
                        podio_sync = eliminatorias_sync(clasificados_sync)
                        connection.sendall(str(podio_sync).encode('utf-8'))
                    elif data.decode('utf-8') == "reporte":
                        # how to send a file to the client
                        with open('reporte.txt', 'rb') as f:
                            l = f.read(1024)
                            while (l):
                                connection.send(l)
                                print('Sent ',repr(l))
                                l = f.read(1024)
                            f.close()
                            print('Done sending')
                    else:
                        # h) Recibir nombre del cliente y enviarle el mensaje de confirmacion
                        confirmacion = "Procesando data"
                        connection.sendall(confirmacion.encode())
                else:
                    print("No hay mas datos de", cliente_address)
                    break
        except Exception as e:
            print("Error en la conexion: ", e)
        finally:
            connection.close()