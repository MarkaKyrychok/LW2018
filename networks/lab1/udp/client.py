import socket
import struct


SERVER_ADDRESS = ('localhost', 3001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    print('Client sending 3 integers')
    for data in [1, 4, 8]:
        sock.sendto(struct.pack('i', data), SERVER_ADDRESS)
        print('Client send:', data)

    print('Client sending 9 chars')
    for data in 'abcdefghi':
        sock.sendto(data.encode(), SERVER_ADDRESS)
        print('Client send:', data)

finally:
    sock.close()
