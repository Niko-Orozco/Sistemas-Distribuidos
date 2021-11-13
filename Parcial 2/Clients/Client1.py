import numpy as np
import socket
import json


"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANREI OROZCO
"""
client_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client Socket Created')
host = 'localhost'
port = 5433

"""
WHAT DOES THE USER NEED?
CREATE, DELETE, ENTER OR EXIT ANY GROUP. ANY USER MAY BE PART OF ANY GROUP
LIST THE EXISTING GROUPS
SEND A MESSAGE TO ANY GROUP
"""
def main():
    userControler()


def userControler():
    option = True
    while option:
        print("---------Welcome to our service---------")
        print("Press 1 to create a group")



if __name__ == "__main__":
    main()
