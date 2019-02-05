import socket 
host = input("Enter a host: ")
target = socket.gethostbyname(host)
print(target)
