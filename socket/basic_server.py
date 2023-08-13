# RUN THIS SCRIPT BEFORE BASIC_CLIENT.py

import socket

# Opening
# Server: B-L-A (Bind-Listen-Accept)
my_socket = socket.socket()
my_socket.bind(("127.0.0.1", 12345))
my_socket.listen()
new_socket, address = my_socket.accept()

# Sending - must be in bytes
new_socket.sendall(b"Hello from the server")

# Receiving
data = new_socket.recv(1024)
print("Data received:", data.decode())

# Closing
new_socket.close()
my_socket.close()