from socket import *
serverHost = "127.0.0.1" # Loopback address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost,serverPort))

print("Local : " , clientSocket.getsockname())
print("Remote: ", clientSocket.getpeername())
while True:
    toServer = input("Send to server (q to quit): ")
    if toServer == 'q':
        break
    clientSocket.send(toServer.encode())
    print("Waiting for the server response...")
            # wait until something is received (blocking socket)
    fromServer = clientSocket.recv(1024).decode()
    print("From Server: ", fromServer)

clientSocket.close()
# Note you can open two instances of Python IDLE. One to run the
# server code and the other to run the client code.
