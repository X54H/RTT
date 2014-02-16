import socket
import time

import mysocket
import utils

def TCP(host, port, msgsize, bufsize):
    """Measures round-trip time (RTT) in seconds over TCP to host:port for a
    message of size 2**msgsize bytes in chunks of size 2**bufsize bytes.

    Returns None if there are any errors."""
    server = mysocket.MySocket(type=socket.SOCK_STREAM)

    sizemsg = (chr(msgsize) + chr(bufsize)).encode()

    msgsize, bufsize = 2**msgsize, 2**bufsize

    msg = utils.makebytes(msgsize)

    try:
        server.connect((host, port))

    except socket.error:
        return None

    try:
        # inform server of msgsize and bufsize
        server.sendall(sizemsg)
        # await confirmation before sending message
        server.recv(1)

        start_time = time.time()
        server.sendby(msg, msgsize, bufsize)
        recvmsg = server.recvby(msgsize, bufsize)
        end_time = time.time()

        return end_time - start_time
        
    finally:
        server.close()

def UDP(host, port, msgsize, bufsize):
    print("UDP RTT client not yet implemented")
