import socket
import os
s = socket.socket()
host = '127.0.0.1'
port = 4444
s.connect((host, port))
print("Starting Client")
filename = 'received_file.txt'
print("***********")
print("File Content:")
with open(filename, 'wb') as f:
    while True:
        data = s.recv(1024)
        f.write(data)
        print(data.decode())
        if not data:
            break
    
print("***********")
f.close()
print('Successfully received the file\nFilename:',filename)
d = os.path.getsize('received_file.txt')
print("File size: ",d)
s.close()