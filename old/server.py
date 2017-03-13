from socket import *


HOST = ''
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
#(client,(ip,port))=s.accept()\
conn, addr = s.accept()
print('Connected by: ', addr)
while True:
        data = conn.recv(1024)
        print("Received: ", repr(data))
        reply = input("Reply: ")
        reply_enc = str.encode(reply)
        type(reply_enc)
        conn.sendall(reply_enc)

conn.close()










##import socket
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##ip_address = ""
###ip_address = "192.168.43.160"
##port = 8000

###sock.bind("192.168.43.160",8000)
##sock.bind((ip_address, port))
##sock.listen(2)
##(client,(ip,port))=sock.accept()

##client.send("Is this working yet?")







#from socket import *

#HOST = '127.0.0.1'
#PORT = 8000
#s = socket(AF_INET, SOCK_STREAM)
#s.connect((HOST, PORT))
#while True:
#        message = raw_input("Your Message: ")
#        s.send(message)
#        print ("Awaiting reply: ")
#        reply = s.recv(1024)
#        print ("Received: ", repr(reply))

#s.close()