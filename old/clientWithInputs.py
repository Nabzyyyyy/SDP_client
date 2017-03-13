from socket import *
import datetime
import json
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) 

def send_data(strdt):
	message = strdt
	bytes = str.encode(message)
	type(bytes)
	s.send(bytes)							
	print("Awaiting confirmation...")
	reply = s.recv(1024)
	print("Received: ", repr(reply))
	return None

#HOST = '192.168.1.189'
HOST = '192.168.43.160'
#HOST = '192.168.43.183'
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
	#Log info to be sent to server
dt = datetime.datetime.now()
dt = dt.replace(microsecond=0)
datestring = str(dt)
#plate = 'EDK6023'
plate = "GJH9885"
access = True
logEntry = (datestring, plate, access)  #does this work?


jsonLog = json.dumps(logEntry)

send_data(jsonLog)
#send_data(datestring)
#send_data(plate)
#send_data(access)
while True:
        x = 1
s.close()


#while True

# def mysend(sock, msg):
# 	totalsent = 0
# 	while totalsent < MSGLEN:
# 		sent = sock.send(msg[totalsent:])
# 		if sent == 0:
# 			raise RuntimeError("socket connection broken")
# 		totalsent = totalsent + sent

#msg = logEntry
#mysend(s, logEntry)


#s.socket(AF_INET, SOCK_STREAM)

#s.connect((HOST, PORT))

#s.close()
