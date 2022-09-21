import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
    data = conn.recv(1024).decode()
    if data == "exit":
        break
    print(data)

conn.close()
