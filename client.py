from socket import *
import datetime
import json

        
#HOST = '192.168.1.189'
HOST = '192.168.43.160'
#HOST = '192.168.43.183'
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))


def send_data(strdt):
	message = strdt
	bytes = str.encode(message)
	type(bytes)
	s.send(bytes)							
	print("Awaiting confirmation...")
	reply = s.recv(1024)
	print("Received: ", repr(reply))
	s.close()

#creates dummy log info to be sent to server
def createLog():
        dt = datetime.datetime.now()
        dt = dt.replace(microsecond=0)
        datestring = str(dt)
        #plate = 'EDK6023'
        plate = "GJH9885"
        access = True
        request = {}
        log = {}
        log['timestamp'] = datestring
        log['plate'] = plate
        log['access'] = access
        request['log'] = log
        request['end'] = True
        jsonLog = json.dumps(request)
        return jsonLog

	

send_data(createLog())

