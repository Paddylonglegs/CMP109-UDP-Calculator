'''
Name: udpCALC_client.py
Desc: an example UDP client
Auth: Patrick Collins
Date: 15/11/19
©️license MIT
https://github.com/Paddylonglegs/
'''
import socket

SERVER_NAME = 'localhost'
SERVER_PORT = 12345

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Getting user inputs

CALC_TYPE = input("input calculation type (+,-,*,/)") # How input calculation type is stored.
USER_MESSAGE1 = input('Input first number ') # How the first number is stored.
USER_MESSAGE2 = input('Input second number ') # How the second number is stored.

#Turning the inputs into one string
All = CALC_TYPE + ',' + USER_MESSAGE1 + ',' + USER_MESSAGE2 #Combining all variables into one. The ',' is so it can be split up server side.


CLIENT_SOCKET.sendto(All.encode(), (SERVER_NAME, SERVER_PORT)) #Encoding this string and sending to the server

MODIFIED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(2048)

print("Calculation: ", MODIFIED_MESSAGE.decode()) #Display the result of calculation.

CLIENT_SOCKET.close()

