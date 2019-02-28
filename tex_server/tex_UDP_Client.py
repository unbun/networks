from socket import *
serverHost = "127.0.0.1" #Loopback address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

toServer = input("To exchange currency enter: <amount> <cur1> <cur2>\n")

while toServer != 'q':
    clientSocket.sendto(toServer.encode(),(serverHost, serverPort))
    fromServer, serverAddress = clientSocket.recvfrom(1024)

    print (fromServer.decode() + "\n")
    toServer = input("To exchange currency enter: <amount> <cur1> <cur2> (q to quit)\n")

print ("User Requested Termination\n")
clientSocket.close()
