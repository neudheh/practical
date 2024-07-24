import socket

addr = input("Enter the IPv4 address of the server: ")
port = input("Enter the port number: ")

chat_socket = socket.socket()
chat_socket.connect((addr, int(port)))

while True:
    # waits for server's message
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    
    # end the program
    if data == b'END\n':
        break
    else:
        print(f"Server says: {data.decode()}")

    # sends a message
    message = input("Send a message to the client (send END to end the chat):")
    message = message.encode() + b'\n'
    chat_socket.sendall(message)

chat_socket.close()