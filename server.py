import socket
import os
port = 4444
s = socket.socket()
host = '127.0.0.1'
s.bind((host, port))
s.listen(5)
print("Server listening...")
while True:
    conn, addr = s.accept()
    print("Connection with {} established".format(addr))
    filename = 'send_client.txt'
    print("Sending file: {}".format(filename))
    bsize = os.path.getsize(filename)
    print("File size: {}".format(bsize))
    file1 = open(filename, 'rb')
    l = file1.read(bsize)
    conn.send(l)
    file1.close()
    print('File sent')
    conn.close()
    break
s.close()