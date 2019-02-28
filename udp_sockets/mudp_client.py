from socket import *
serverHost = "127.0.0.1" #Loopback address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

toServer = input("Send to server:")
while toServer != 'q':
    clientSocket.sendto(toServer.encode(),(serverHost, serverPort))
    print ("Waiting for the server response ...")
    fromServer, serverAddress = clientSocket.recvfrom(1024    )
    print ("From Server:", fromServer.decode())
    toServer = input("Send to server (q to quit): ")
clientSocket.close()
