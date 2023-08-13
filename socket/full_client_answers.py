#CHATBOT

import socket

# Function to choose host and address
def input_host_address(prev_host = -1, prev_address=-1):
    host = input("Enter host (to use default type 'd', to use previous type 'p'): ")
    if host == 'd':
        host = "127.0.0.1"
    elif host == 'p':
        host = "127.0.0.1" if prev_host == -1 else prev_host
    address = input("Enter host (to use default type 'd', to use previous type 'p'): ")
    if address == 'd':
        address = 12345
    elif address == 'p':
        address = 12345 if prev_address == -1 else prev_address
    else:
        address = int(address)
    return host, address

# Setup socket
host, address = input_host_address()
chat_socket = socket.socket()
chat_socket.connect((host, address))
print("Socket opened")

# Function for sending
def send(send_socket):
    to_send = input('What would you wish to send? (Press q to exit)\nEnter message: ')
    while to_send != 'q':
        send_socket.sendall(to_send.encode())
        to_send = input('Enter message: ')
    send_socket.sendall(b'\n')

# Function for receiving
def receive(receive_socket):
    received_message = b''
    new_message = receive_socket.recv(1024)
    while b'\n' not in new_message:
        received_message += new_message + b'\n'
        new_message = receive_socket.recv(1024)
    return received_message.decode()

# Menu for user input send, receive or switch client socket
while True:
    print("-"*15)
    choice = int(input(r'''Menu
1: Restart socket
2: Send message
3. Receive messages
4. Quit
Please input choice: '''))
    print("-"*15)
    if choice == 1:
        chat_socket.close()
        print("Socket closed")
        host, address = input_host_address()
        chat_socket = socket.socket()
        chat_socket.connect((host, address))
        print("Socket reopened")
    elif choice == 2:
        send(chat_socket)
    elif choice == 3:
        print("Waiting for messages")
        message = receive(chat_socket)
        print(message, end='')
    elif choice == 4:
        chat_socket.close()
        print("All sockets closed")
        break