from socket import *
serverHost = "127.0.0.1" #Loopback address
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #create UDP socket

serverSocket.bind((serverHost,serverPort))
print ("The server is ready to receive.")

while True: #loop forever
    print ("Waiting for a message from the Client ...")
    #Read from UDP socket into message, getting client’s address
    fromClient, clientAddress = serverSocket.recvfrom(1024)
    print ("Client:" + str(clientAddress))
    print (" Sent: " + fromClient.decode())
    toClient = fromClient.decode().upper()
    serverSocket.sendto(toClient.encode(), clientAddress)
serverSocket.close()
