from socket import *

#dictionary of every conversion con_factors
#key format: '<cur1>' -> '<cur2>'
con_factors = {'same':  1.0,
                'USD -> EUR' : 0.81,
                'USD -> CAD' : 1.25,
                'USD -> GBP' : 0.72,
                'EUR -> USD' : 1.24,
                'EUR -> CAD' : 1.55,
                'EUR -> GBP' : 0.89,
                'CAD -> USD' : 0.80,
                'CAD -> EUR' : 0.64,
                'CAD -> GBP' : 0.57,
                'GBP -> USD' : 1.40,
                'GBP -> EUR' : 1.13,
                'GBP -> CAD' : 1.75}

# takes in string formatted "<amount> <currency1> <currency2>"
# converts amount in currency1 to amount in currency2
# returns error messages if input string incorrectly formatted
def convert(client_in):

    str_in = str(client_in)

    if str_in == "?":
        str_out = "USD = United States Dollar \n"
        str_out += "EUR = European Euro\n"
        str_out += "CAD = Canadian Dollar\n"
        str_out += "GBP = United Kingdom pound\n"
        return str_out

    try:
        amt, c1, c2 = str_in.split(" ")
        c1 = c1.upper()
        c2 = c2.upper()

    except ValueError: #should be thrown by the split() or upper() function
        return "Error! Not enough values given\n\t(or values formatted incorrectly)"


    if c1 == c2:
        convert_key = 'same' ## saves space in the dictionary
    else:
        convert_key = c1 + " -> " + c2 # fit the format of the dictionary keys

    if convert_key in con_factors: #makes sure the currencies are in the dict
        try:
            new_amt = float(amt) * con_factors[convert_key]
            return str(amt) + " " + c1 + " = " + str(new_amt) + " " + c2
        except ValueError:# thrown by float() or str()
            return "Error! Invalid <amount> value"

    return "Error! Invalid <cur> value(s)" #if convert_key is not in the dict


if __name__ == '__main__':

    serverHost = "127.0.0.1" #Loopback address
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM) #create UDP socket

    serverSocket.bind((serverHost,serverPort))
    print ("The TEX server is ready to receive.")

    while True: #loop forever
        print ("Waiting for TEX conversion request from the Client ...")
        #Read from UDP socket into message, getting client’s address
        fromClient, clientAddress = serverSocket.recvfrom(1024)
        fromClient = fromClient.decode()
        print ("Client:" + str(clientAddress))
        print (" Sent: " + fromClient)

        serverSocket.sendto(convert(fromClient).encode(), clientAddress)

    serverSocket.close()
