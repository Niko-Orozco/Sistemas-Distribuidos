import socket
import json
import time
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

matrix_of_groups =  [['add','m1','m4', 'nm', 'nm'],
                    ['empty', 'nm', 'nm', 'nm', 'nm'],
                    ['mul', 'm1', 'm4', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm']]

matrix_of_clients = [['m1', 'na'],
                     ['m2', 'na'],
                     ['m3', 'na'],
                     ['m4', 'na']]



"""
THIS FUNCTION WILL CREATE A GROUP AND INSERT THE PERSON WHO CREATED IT TO THE GROUP
EDITORS NOTE: THIS FUNCTION IS READY
"""
def addGroupToMatrix(machine_id, information):
    if(information == '1'):
        """
        WE SHALL CREATE AN ADD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'add'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '2'):
        """
        WE SHALL CREATE A SUB GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'sub'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '3'):
        """
        WE SHALL CREATE A MUL GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'mul'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '4'):
        """
        WE SHALL CREATE A DIV GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'div'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '5'):
        """
        WE SHALL CREATE A POW GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'pow'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '6'):
        """
        WE SHALL CREATE A RAD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'rad'
                matrix_of_groups[i][1] = machine_id
                break
    if(information == '7'):
        """
        WE SHALL CREATE A LOG GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'log'
                matrix_of_groups[i][1] = machine_id
                break
"""
THIS FUNCTION WILL CHECK IF A GROUP ALREADY EXISTS
"""
def already_Group(information):
    is_already_group = False
    if(information == '1'):
        """
        USER WANTS TO CREATE AN ADD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'add'):
                is_already_group = True
                break
    if(information == '2'):
        """
        USER WANTS TO CREATE A SUB GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                is_already_group = True
                break
    if(information == '3'):
        """
        USER WANTS TO CREATE A MUL GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'mul'):
                is_already_group = True
                break
    if(information == '4'):
        """
        USER WANTS TO CREATE A DIV GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'div'):
                is_already_group = True
                break
    if(information == '5'):
        """
        USER WANTS TO CREATE A POW GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'pow'):
                is_already_group = True
                break
    if(information == '6'):
        """
        USER WANTS TO CREATE A RAD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'rad'):
                is_already_group = True
                break
    if(information == '7'):
        """
        USER WANTS TO CREATE A LOG GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'log'):
                is_already_group = True
                break
    return is_already_group

"""
THIS FUCNTIION CORRESPONDS TO THE FIRST OPTION IN THE GROUP MANIPULATION OPTIONS
IT WILL ATEMPT TO CREATE A GROUP
IF IT ALREADY EXISTS IT WILL TELL THE USER
"""
def create_Group(machine_id, information, client_addr):
    print("The user has elected to create a group")
    is_already_group = False
    option = True
    while option:
        if(information == '1'):
            """
            THE USER HAS CHOSEN TO CREATE AN ADD GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '2'):
            """
            THE USER HAS CHOSEN TO CREATE A SUB GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '3'):
            """
            THE USER HAS CHOSEN TO CREATE A MUL GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '4'):
            """
            THE USER HAS CHOSEN TO CREATE A DIV GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '5'):
            """
            THE USER HAS CHOSEN TO CREATE A POW GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '6'):
            """
            THE USER HAS CHOSEN TO CREATE A RAD GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)
        if(information == '7'):
            """
            THE USER HAS CHOSEN TO CREATE A LOG GROUP
            """
            is_already_group = already_Group(information)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, information)
                    print("New matrix of groups")
                    print(matrix_of_groups)
                    """
                    WE SHOULD HAVE THE UPDATED MATRIX TO SEND TO USER
                    WILL HAVE TO DO ON A JSON
                    """
                    group_data = json.dumps({"matrix": matrix_of_groups})


                    data_Set = {"groups": matrix_of_groups}
                    data = json.dumps(data_Set)
                    print("About to show what is in data")
                    print(data)

                    try:
                        server_socket.sendto(data.encode(), client_addr)

                        confirmation_message, client_addr = server_socket.recvfrom(4096)
                        confirmation_message = confirmation_message.decode()
                        if(confirmation_message == "Proceed"):
                            handle_Client(machine_id, client_addr)
                    except Exception as e:
                        print(e)



"""
THIS FUNCTION WILL COVER THE BASIC INTERACTION BETWEEN THE CLIENTS CHOSEN GROUP MANIPULATION FUNCTION
"""
def group_Manipulation(machine_id, information, client_addr):
    option = True
    while option:
        """
        FOR INFORMATION
        1 CREATE GROUP
        2 DELETE GROUP
        3 ENTER GROUP
        4 EXIT GROUP
        5 VIEW ALL GROUPS
        6 TEXT A GROUP
        """
        if(information == '1'):
            """
            THE CLIENT HAS CHOSEN TO CREATE AN ADD GROUP
            """
            create_Group(machine_id, information, client_addr)
        if(information == '2'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A SUBTRACT GROUP
            """
            create_Group(machine_id, information, client_addr)
        if(information == '3'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A MULTIPLY GROUP
            """
            create_Group(machine_id, information, client_addr)
        if(information == '4'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A DIVIDE GROUP
            """
            create_Group(machine_id, information, client_addr)
        if(information == '5'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A POWER GROUP
            """
            create_Group(machine_id, information, client_addr)
        if(information == '6'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A RADICAL GROUP !OH NO :(
            """
            create_Group(machine_id, information, client_addr)
        if(information == '7'):
            """
            THE CLIENT HAS CHOSEN TO CREATE A LOGARITHM GROUP
            """
            create_Group(machine_id, information, client_addr)
"""
THIS FUNCTION HANDLES THE CLIENTS REQUESTS AND ROUTES THEM ACCORDINGLY
"""
def handle_Client(machine_id, client_addr):
    option = True
    while option:
        data, client_addr = server_socket.recvfrom(4096)
        if data:
            data = json.loads(data.decode())
            array_data = data.get("data")
            machine_id = array_data[0]
            operation = array_data[1]
            information = array_data[2]
            print("Machine id: ", machine_id)
            print("Operation: ", operation)
            print("Information: ", information)
            """
            THINK ABOUT THIS SEND
            MAYBE SAVE IT FOR THE RESULT
            """
            server_socket.sendto("Recieved data".encode(), client_addr)

            message, client_addr = server_socket.recvfrom(4096)
            message = message.decode()
            """
            UP TO THIS POINT WE HAVE CONFIRMED THAT THE CLIENT AND SERVER HAVE SENT
            US THE INFORMATION
            AND NOW WE SHALL PROCEED WITH HIS REQUEST
            """
            if(message == 'Proceed'):
                """
                OPERATION
                1 MEANS GROUP MATRIX MANIPULATION
                """
                if(operation == '1'):
                    group_Manipulation(machine_id, information, client_addr)



"""
THE ADD CLIENT FUNCTION WILL ADD A CLIENT TO THE MATRIX OF CLIENTS WITH HIS ID AND ADDRESS
"""
def add_Client(machine_id, client_addr):
    for i in range(len(matrix_of_clients)):
        if(matrix_of_clients[i][0] == machine_id):
            matrix_of_clients[i][1] = client_addr
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
        machine_id, client_addr = server_socket.recvfrom(4096)
        machine_id = machine_id.decode()
        print("Connection established with ", machine_id, "@ address ", client_addr)
        """
        SENDING CONFIRMATION MESSAGE THAT MACHINE ID HAS BEEN RECIEVED
        """
        server_socket.sendto("Recieved machine id".encode(), client_addr)

        add_Client(machine_id, client_addr)
        print("New matrix of clients: ")
        print(matrix_of_clients)

        handle_Client(machine_id, client_addr)

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
