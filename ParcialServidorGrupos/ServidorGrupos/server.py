import socket
import json

"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANDREI OROZCO
"""

host = 'localhost'
port =  5432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Group server socket created")

server_socket.bind((host, port))
print("Group server socket connected to ", host)

matrix_Of_Groups =  [['add','m4','m1', 'nm', 'nm'],
                    ['sub', 'm2', 'm3', 'nm', 'nm'],
                    ['mul', 'm1', 'm4', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm']]

matrix_Of_Clients = [['m1', 'na'],
                     ['m2', 'na'],
                     ['m3', 'na'],
                     ['m4', 'na']]



def handle_Client(machine_ID, client_addr):
    option = True
    while option:
        data, client_addr = server_socket.recvfrom(4096)

"""
THE ADD CLIENT FUNCTION WILL ADD A CLIENT TO THE MATRIX OF CLIENTS WITH HIS ID AND ADDRESS
"""
def add_Client(machine_ID, client_addr):
    for i in range(len(matrix_Of_Clients)):
        if(matrix_Of_Clients[i][0] == machine_ID):
            matrix_Of_Clients[i][1] = client_addr
            break

def main_Control():
    option = True
    while option:
        """
        THIS FIRST BLOCK OF CODE ENSURED THAT WE ARE RECIEVING NEW CLIENTS
        EVENTUALLY THE IDEA IS TO HAVE EACH CLIENT ON A THREAD OR SOMETHING SIMILAR
        """
        print("Group server is listening...")
        """
        REVIEVING MACHINE ID AND ADDRESS FOR CLIENT
        """
        machine_ID, client_addr = server_socket.recvfrom(4096)
        machine_ID = machine_ID.decode()
        print("Connection established with ", machine_ID, "@ address ", client_addr)
        """
        SENDING CONFIRMATION MESSAGE THAT MACHINE ID HAS BEEN RECIEVED
        """
        server_socket.sendto("Recieved machine id".encode(), client_addr)

        add_Client(machine_ID, client_addr)
        print("New matrix of clients: ")
        print(matrix_Of_Clients)

        handle_Client(machine_ ID, client_addr)

def main():
    """
    The matrix of groups has a total of 7 rows representing the different groups
    The matrix of groups has a total of 3 columns, the first to identity the groups
    The first element of each row represents the group id
    the rest of the elements en in each row represent the members of that group
    When a group does not exist the group id is replaced with (empty)
    When the group has spots available, those spots are filled with (nm) representing NO MEMBER
    """
    main_Control()

if __name__ == "__main__":
    main()
