import socket
import os

PORT = 9065

def process(req):
 #   if req == 'look':
 #      return os.getcwd()
    if req == 'look': 
        return '; '.join(os.listdir())
 #  elif req == 'touch': #sozdanie file
 #      return '; '.join(os.touch())
    elif req == 'mkdir': #sozdanie papka
        name=conn.recv(1024).decode()
        try:
        	print(name)
        	os.mkdir(name)
        	return "OK"
        except:
            return "Fail"
 #delite papka   
    elif req == 'deldir': 
        name1=conn.recv(1024).decode()
        try:
            print(name1)
            os.rmdir(name1)
            return "OK"
        except:
            return "Fail"
    else:
        return 'bad request'

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()

while True:
    print("Port:",PORT)
    conn, addr = sock.accept()
    print(addr)

    request = conn.recv(1024).decode()
    print(request)
    response = process(request)
    conn.send(response.encode())

sock.close()
