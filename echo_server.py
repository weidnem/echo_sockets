import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    #create socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #bind to address
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    
    try:
        while True:
            # the outer loop controls the creation of new connection sockets. The
            # server will handle each incoming connection one at a time.
    
            sock.listen(1)
            print('waiting for a connection', file=log_buffer)
    
            # make a new socket when a client connects, call it 'conn',
            conn, addr = sock.accept()
            print('connection - {0}:{1}'.format(*addr), file=log_buffer)
            
            while True:
                
                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                data = conn.recv(16)
                if not data:
                    #close connection on no data
                    conn.close()
                    print('echo complete, client connection closed', file=log_buffer)
                    break #break out of this loop, outer loop waits for new connection
                    
                print('received "{0}"'.format(data.decode('utf8')))
                conn.send(data)
                print('sent "{0}"'.format(data.decode('utf8')))

    except KeyboardInterrupt:
        # Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.

        sock.close()
        print('quitting echo server', file=log_buffer)

    finally:
        sock.close()


if __name__ == '__main__':
    print("started")
    server()
    sys.exit(0)