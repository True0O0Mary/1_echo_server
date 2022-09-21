import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))

#msg = input()
msg = ""
while True:
    msg = input()
    if msg == "exit":
        break
    sock.send(msg.encode())
    
sock.close()

