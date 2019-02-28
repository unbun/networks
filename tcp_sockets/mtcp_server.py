from socket import* #import everything from socket
                    #to avoid having socket as a prefix to its objects
serverHost = "127.0.0.1" #Loopback address
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
                #create TCP welcoming socket

serverSocket.bind((serverHost,serverPort))
serverSocket.listen(2)
        #1 is the backlog parameter that specifies the maximum number
        # of connections requests that the kernel should queue
        # for this socket waiting for completion of the connection.
print("The server is ready to receive")
#waits on for incoming requests. New socket created on return
connectionSocket, addr = serverSocket.accept()
#print ip address and port number of the local and remote hosts
print ("Local : " , connectionSocket.getsockname())
print("Remote:", connectionSocket.getpeername())

while True: #loop forever
    print("Waiting for a message from the Client ...")
    fromClient = connectionSocket.recv(1024).decode()
        # wait until (blocking socket) receiving a max of 1024
        # bytes at a time and decode the received UTF‐8 string
        # to Unicode string.
        # Unicode text is the default string type in Python3
    if not (fromClient):
        break
    print("from connected client:", fromClient)
    toClient = fromClient.upper()
    connectionSocket.send(toClient.encode())
        #encoding a default Unicode string to UTF‐8
connectionSocket.close() #close connection to this client
                        #(but not welcoming socket)
