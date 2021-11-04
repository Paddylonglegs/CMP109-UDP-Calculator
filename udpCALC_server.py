'''
Name: udpCALC_server.py
Desc: an example UDP server
Auth: Patrick Collins
Date: 15/11/19
©️license MIT
https://github.com/Paddylonglegs/
'''

import socket

SERVER_PORT = 12345

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_SOCKET.bind(('localhost', SERVER_PORT))
print('the server is ready') #Letting the user know the server is ready to recieve messages.

INCOMING_MESSAGE, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
print(' Incoming Calculation: ', INCOMING_MESSAGE)  #Recieving the client message.
print(' Incoming Calculation: ', INCOMING_MESSAGE.decode()) #Decoding the message from the client.


INCOMING_MESSAGE = INCOMING_MESSAGE.decode().split(',') #Decoding and Splitting the message

#Checking the calculation type

if INCOMING_MESSAGE[0] == '+':
    CALC = int(INCOMING_MESSAGE[1]) + int(INCOMING_MESSAGE[2]) #Adding the two numbers together
    


if INCOMING_MESSAGE[0] == '-':
   CALC = int(INCOMING_MESSAGE[1]) - int(INCOMING_MESSAGE[2]) #Subtracting the two numbers
   


if INCOMING_MESSAGE[0] == '*':
    CALC = int(INCOMING_MESSAGE[1]) * int(INCOMING_MESSAGE[2]) #Multiplying two numbers
    


if INCOMING_MESSAGE[0] == '/':
    CALC = int(INCOMING_MESSAGE[1]) / int(INCOMING_MESSAGE[2]) #Dividing two numbers
    

CALCULATION = str(CALC) #Converting the calculation to a string


print("Calculation: ", CALCULATION) #Printing the calculation in the server


SERVER_SOCKET.sendto(CALCULATION.encode(), CLIENT_ADDRESS) #Encoding the calculation and sending it back to the client

SERVER_SOCKET.close()
