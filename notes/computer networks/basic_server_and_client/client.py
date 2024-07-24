import socket

my_socket = socket.socket()

address = input("Enter the IPv4 address of the server: ")
port = int(input("Enter the port number: "))

my_socket.connect((address, port))

data = b""
#/n to show that a message has terminated
while b"\n" not in data:
    # recieves information
    data += my_socket.recv(1024) 
    # an argument for recieve is needed, 
    # and usually people use 1024
print(data)
my_socket.close()