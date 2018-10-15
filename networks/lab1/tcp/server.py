import socket
import struct


SERVER_ADDRESS = ('localhost', 3001)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SERVER_ADDRESS)
sock.listen()

int_size = struct.calcsize('i')

while True:
    print('Waiting for connection...')

    connection, client_address = sock.accept()
    print('Connection from', client_address)

    try:
        for i in range(3):
            data = connection.recv(int_size)
            print('Received', struct.unpack('i', data)[0])

        for i in range(9):
            data = connection.recv(1)
            print('Received', data.decode())

    finally:
        connection.close()
