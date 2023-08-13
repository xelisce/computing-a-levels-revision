# CHATBOT

import socket

# Function to choose host and address
def input_host_address():
    host = input("Enter host (to use default type 'd'): ")
    host = host if host != 'd' else "127.0.0.1"
    address = input("Enter host (to use default type 'd'): ")
    address = int(address) if address != 'd' else 12345
    return host, address

# Setup socket
host, address = input_host_address()
listen_socket = socket.socket()
listen_socket.bind((host, address))
print("Listening for client...")
listen_socket.listen()
chat_socket, address = listen_socket.accept()
print("Client found at address", address)

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

# Menu for user input send or switch client socket
while True:
    print("-"*15)
    choice = int(input(r'''Menu
1: Switch socket
2. Send message
3. Receive messages
4. Quit
Please input choice: '''))
    print("-"*15)
    if choice == 1:
        chat_socket.close()
        print("Listening for client...")
        chat_socket, address = listen_socket.accept()
        print("Client found at address", address)
    elif choice == 2:
        send(chat_socket)
    elif choice == 3:
        print("Waiting for messages...")
        message = receive(chat_socket)
        print(message, end='')
    elif choice == 4:
        chat_socket.close()
        listen_socket.close()
        print("All sockets closed")
        break