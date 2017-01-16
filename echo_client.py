import socket
import sys


def client(msg, log_buffer=sys.stderr):
    #set server address
    server_address = ('localhost', 10000)

    #create socket and connect to server
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)
    
    #send message
    print('sending "{0}"'.format(msg), file=log_buffer)
    sock.sendall(msg.encode('utf8'))
    print("done Sending")
    

    try:
        #set empty variables
        received_message = ''
        chunk = ''
       
        while True: #loop controls reciving echo message
            chunk = sock.recv(16)
            if not chunk:
                break #break out of loop on no data
            
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            #build message
            received_message += chunk.decode('utf8')
            
            if received_message == msg:
                break #break out of loop if messages match
                
    finally:
        #clean-up and close connection
        print('closing socket', file=log_buffer)
        sock.close()
        return received_message

if __name__ == '__main__':
    print('hih')
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
