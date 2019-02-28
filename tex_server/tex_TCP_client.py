from socket import *
serverHost = "127.0.0.1" # Loopback address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost,serverPort))

print("Local : " , clientSocket.getsockname())
print("Remote: ", clientSocket.getpeername())
print("***************************\n\n")


while True:
    toServer = input("To exchange currency enter: <amount> <cur1> <cur2> (q to quit)\n")
    if toServer == 'q':
        break

    clientSocket.send(toServer.encode())
    fromServer = clientSocket.recv(1024).decode()
    print(fromServer + "\n")

print ("\n\n***************************")
print ("User Requested Termination\n")
clientSocket.close()
