from socket import *
import datetime

HOST = ''
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
#(client,(ip,port))=s.accept()\
conn, addr = s.accept()
print('Connected by: ', addr)
dt = datetime.datetime.now()
dt = dt.replace(microsecond=0)
plate = 'EDK6023'
access = True
#logEntry = (dt, plate, access)  #does this work?

#while True:

	#data = conn.recv(1024)
	#print("Received: ", repr(data))
	#reply = input("Reply: ")
	#reply_enc = str.encode(reply)
	#type(reply_enc)
	#conn.sendall(reply_enc)


conn.close()