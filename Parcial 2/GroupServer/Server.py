import socket
import json


HEADER_LENGTH = 10
host = 'localhost'
port = 5432
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Group server socket created")

server_socket.bind((host, port))
print("Group server socket connected to: ", localhost)

matrix_of_groups =  [['add','m4','m1', 'nm', 'nm'],
                    ['sub', 'm2', 'm3', 'nm', 'nm'],
                    ['mul', 'm1', 'm4', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm']]

matrix_of_clients = [['m1', 'na'],
                     ['m2', 'na'],
                     ['m3', 'na'],
                     ['m4', 'na']]

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

"""
THIS FUNCTION ADDS A CLIENT WITH ITS ADDRESS TO THE CLIENTS MATRIX
"""
def add_Client():
    for i in range(len(matrix_of_clients)):
        if(matrix_of_clients[i][0] == machine_id):
            matrix_of_clients[i][1] = address
            break
    return matrix_of_clients


"""
THIS FUNCTION WILL HANDLE THE REQUESTS FROM THE CLIENTS
AND WILL ROUTE THE REQUEST ACCORDINGLY
"""
def handle_Client(client_information):
    client = client_information[0]
    machine_id = client_information[1]
    option = True
    while option:
        try:
            data = client.recv(4096)
            if data:
                print("Data recieved successfully")
                data = json.loads(data.decode())
                """
                MACHINE ID WILL HELP US IDENTIFY EACH SEPARATE USER
                EACH MACHINE IS ASSIGNED AN ID AS SOONAS CREATED
                M1
                M2
                M3 ETC
                """
                machine_id = data.get("machine")
                """
                THE OPERATION VARIABLE WILL TELL ME IF THE USER WANTS TO:
                EXECUTE AN OPERATION FROM THE GROUP MANIPULATION PERSPECTIVE, IE CREATE, DELETE, ETC
                EXECUTE A MATHEMATICA OPERATION ADD, SUB, MULY, DIVIDE
                TURN IN A RESULT FROM A REQUEST GIVEN BY THE SERVER
                """
                operation = data.get("operation")
                """
                THE INFORMATION VARIABLE WILL CONTAIN INFORMATION DEPENDING ON THE OPERATION SENT BY USER
                THE GROUP MANIPULATIONS ARE REPRESENTED FORM 1 TO 6
                THE MATHEMATICAL OPERATIONS ARE REPRESENTED FROM 1 TO 7
                THE RESULT IS REPRESENTED BY WHATEVER NUMBER THAT RESULT MAY BE
                """
                information = data.get("information")
                """
                """
                if(operation == 'group'):
                    print("The user wants to manipulate the matrix of groups")
                    """
                    WE SHALL DEAL WITH THE OPTIONS IN ORDER
                    1 CREATE GROUP // NOT CREATED
                    2 DELETE GROUP // NOT CREATED
                    3 ENTER GROUP // NOT CREATED
                    4 EXIT A GROUP // NOT CREATED
                    5 SHOW THE MATRIX OF GROUPS // NOT CREATED
                    6 SEND A MESSAGE TO ALL MEMBERS OF A GROUP // NOT CREATED
                    """
                    if(operation == '1'):

        except:
            client.close()
            for i in range(len(matrix_of_clients)):
                if(matrix_of_clients[i][0] == machine_id):
                    matrix_of_clients[i][1] = 'na'
                    break
"""
THIS FUNCTION IS RESPONSABLE FOR HANDDLING INCOMING MESSAGES AND
IT WILL EITHER HANDDLE A NEW CLIENT OR A PRE-EXISTING ONE
"""
def main_Control():
    option = True
    while option:
        print("Group Server is running and listening...")
        client, address = server.accept()
        print("Connection is established with ", {str(address)})
        client.send("MachineID".encode("utf-8"))
        machine_id = client.recv(1024).decode("utf-8")
        matrix_of_clients = add_Client(machine_id, address)
        client_information = [client, machine_ID]
        handle_Client(client_information)


if __name__ == "__main__":
    main()
