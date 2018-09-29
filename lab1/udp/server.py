import socket
import struct


SERVER_ADDRESS = ('localhost', 3001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SERVER_ADDRESS)
int_size = struct.calcsize('i')

print('Waiting for client..')

for i in range(3):
    data, client_address = sock.recvfrom(int_size)
    print('Received data from', client_address, ':', struct.unpack('i', data)[0])

for i in range(9):
    data, client_address = sock.recvfrom(1)
    print('Received data from', client_address, ':', data.decode())
