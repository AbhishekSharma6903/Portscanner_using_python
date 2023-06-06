

import socket
import termcolor

def scan(target, ports):
	print(termcolor.colored('\n' + 'Starting Scan For ' + str(target),'red'))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Enter Targets To Scan (split by ','): ")
ports = int (input("[*] Enter How Many Ports Tou Want To Scan: ")) 
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"),'green'))
	for ip_address in targets.split(','):
		scan(ip_address.strip(' '), ports)
else:
	scan(targets,ports)
