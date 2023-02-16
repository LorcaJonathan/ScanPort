#!/usr/bin/python3

import nmap
from colorama import Fore,Style

print(Fore.MAGENTA)
print(Style.BRIGHT)
print('  _____                                   _____                       ')
print(' / ____/    ____       __       _    _   |  __ \   ______     _____     _______')
print(' | |___    / ___\     /  \     |  \ | |  |  ___/  /  __  \   /  ___ \  |__   __|')
print(' \____ \  | /        / /\ \    | | \| |  | /     /  /  \  \  |  __  /     | |')
print('  ___/ /  | \___    / /__\ \   | |\ | |  | |     \  \__/  /  | |  \ \     | |')
print(' |____/    \____\  /_/    \_\  |_| \ _|  |_|      \______/   |_|   \_\    |_|')
print('')

print(Fore.BLUE + '\n[+] Herramienta que nos permite escaner los puertos abiertos indicando una dirección IP.\n')

ip = input('[+] Introduce la ip del host que quieres escanear: ' + Fore.WHITE)
print(Fore.YELLOW + '\nBuscando puertos abiertos...' + Fore.WHITE)
nm = nmap.PortScanner()
results = nm.scan(ip)
count = 0

print('\nIP host : %s' % ip)
print('State : %s\n' % nm[ip].state())
for proto in nm[ip].all_protocols():
	print('Protocol : %s\n' % proto)
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ('port : %s\tstate : %s' % (port, nm[ip][proto][port]['state']))
		if count == 0:
			open_ports = str(port)
			count = 1
		else:
			open_ports = open_ports + ',' + str(port)
print(Fore.GREEN + '\nLos puertos abiertos son --> ' + Fore.WHITE + open_ports)


































