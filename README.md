# CMP109-UDP-Calculator
Simple calculator using UDP python server and client

UDP Calculator

Client: import socket is used, the user is asked for 3 inputs. Calculation type and 2 numbers which the calculation will be carried out on. The Variables are all made into one variable/string so it can be sent across to the server. The returned message from the server is decoded and displayed showing the user their calculation.

Server: import socket is used, displayed message lets the user know the server is ready. The message receieved from the udpCALC client is split up to get the 3 sepearate inputs that the user entered. The if statements determines which calculation is to be carried out and carries out this calculation with the other 2 split up messages. The calculation is then turned into a string again to return back to the client. The calculation variable is encoded and returned back to the client.  
