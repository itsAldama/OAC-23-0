#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
import threading
import socket
import struct

servidores_ntp = [
	"0.uk.pool.ntp.org",
	"1.es.pool.ntp.org",
	"0.br.pool.ntp.org",
	"2.cl.pool.ntp.org",
	"2.co.pool.ntp.org",
	"0.hk.pool.ntp.org",
	"0.sg.pool.ntp.org",
	"0.jp.pool.ntp.org",
	"0.au.pool.ntp.org",
	"0.nz.pool.ntp.org",
	"0.za.pool.ntp.org",
	"0.fr.pool.ntp.org",
	"0.in.pool.ntp.org",
	"0.tw.pool.ntp.org"
]

"""
Función: get_ntp_time
Descripción: Imprime la hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Ninguna, solo imprime la hora 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 6 * 3600], 'es': ['España', 7 * 3600], 'br': ['Brazil', 2 * 3600],
	                 'cl': ['Chile', 1 * 3600], 'co': ['Colombia', 0], 'hk': ['Hong Kong', 13 * 3600],
	                 'sg': ['Singapur', 13 * 3600], 'jp': ['Japón', 14 * 3600], 'au': ['Australia', 15 * 3600],
	                 'nz': ['Nueva Zelanda', 17 * 3600], 'za': ['Sudáfrica', 7 * 3600], 'fr': ['Francia', 7 * 3600],
	                 'in': ['India', 10.5 * 3600], 'tw': ['Taiwan', 13 * 3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.fromtimestamp(t + timezone_dict[key][1])}")


if __name__ == '__main__':
	# Escriba aquí su código para la parte a


	# Escriba aquí su código para la parte b (puede hacerlo en un archivo separado también, ambas opciones son válidas)
