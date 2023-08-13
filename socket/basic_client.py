# RUN BASIC_SERVER.PY BEFORE THIS SCRIPT

import socket

# Opening
# Client: C (Connect)
my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 12345))

# Sending - must be in bytes
my_socket.sendall(b"Hello from the client")

# Receiving
data = my_socket.recv(1024)
print("Data received:", data.decode())

# Closing
my_socket.close()