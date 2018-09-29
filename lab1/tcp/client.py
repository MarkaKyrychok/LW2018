import socket
import struct


SERVER_ADDRESS = ('localhost', 3001)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER_ADDRESS)
print('Client connected')


try:
    print('Client sending 3 integers')
    for data in [1, 4, 8]:
        sock.sendall(struct.pack('i', data))
        print('Client send:', data)

    print('Client sending 9 chars')
    for data in 'abcdefghi':
        sock.sendall(data.encode())
        print('Client send:', data)
finally:
    sock.close()
