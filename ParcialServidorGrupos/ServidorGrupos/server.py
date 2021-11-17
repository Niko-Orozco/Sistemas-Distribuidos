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

matrix_of_groups =  [['add','m1','m2', 'm4', 'nm'],
                    ['sub', 'm3', 'm4', 'nm', 'nm'],
                    ['mul', 'm1', 'm4', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['log','m2','m3', 'nm', 'nm']]

matrix_of_clients = [['m1', 'na'],
                     ['m2', 'na'],
                     ['m3', 'na'],
                     ['m4', 'na']]





def leave_Group(machine_id, detail):
    if(detail == '1'):
        print("\n")
        print("You are exiting the add group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'add'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j + 1] == machine_id):
                        matrix_of_groups[i][j + 1] = "nm"
                        break
    if(detail == '2'):
        print("\n")
        print("You are exiting the sub group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j + 1] == machine_id):
                        matrix_of_groups[i][j + 1] = "nm"
                        break
    if(detail == '3'):
        print("\n")
        print("You are exiting the sub group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j + 1] == machine_id):
                        matrix_of_groups[i][j + 1] = "nm"
                        break

def exit_Group(machine_id, information, client_addr, detail):
    print("The user has chosen to enter a group")
    group_exists = False
    is_member = False
    option = True
    while option:
        if(detail == '1'):
            """
            THE USER HAS CHOSEN TO ENTER AN ADD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '2'):
            """
            THE USER HAS CHOSEN TO ENTER AN SUB GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '3'):
            """
            THE USER HAS CHOSEN TO ENTER AN MUL GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '4'):
            """
            THE USER HAS CHOSEN TO ENTER AN DIV GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '5'):
            """
            THE USER HAS CHOSEN TO ENTER AN POW GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '6'):
            """
            THE USER HAS CHOSEN TO ENTER AN RAD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '7'):
            """
            THE USER HAS CHOSEN TO ENTER AN LOG GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        leave_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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


def already_In_Group(machine_id, detail):
    is_member = False
    if(detail == '1'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'add'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '2'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '3'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'mul'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '4'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'div'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '5'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'pow'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '6'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'rad'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    if(detail == '7'):
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'log'):
                for j in range(len(matrix_of_groups[i]) - 1):
                    if(matrix_of_groups[i][j+1] == machine_id):
                        is_member = True
                        break
    return is_member


def join_Group(machine_id, detail):
    if(detail == '1'):
        print("The user is joining the add group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'add'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '2'):
        print("The user is joining the sub group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '3'):
        print("The user is joining the mul group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'mul'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '4'):
        print("The user is joining the div group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'div'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '5'):
        print("The user is joining the pow group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'pow'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '6'):
        print("The user is joining the rad group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'rad'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break
    if(detail == '7'):
        print("The user is joining the log group")
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'log'):
                for j in range(len(matrix_of_groups) - 1):
                    if(matrix_of_groups[i][j + 1] == "nm"):
                        matrix_of_groups[i][j + 1] = machine_id
                        break

def enter_Group(machine_id, information, client_addr, detail):
    print("The user has chosen to enter a group")
    group_exists = False
    is_member = False
    option = True
    while option:
        if(detail == '1'):
            """
            THE USER HAS CHOSEN TO ENTER AN ADD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '2'):
            """
            THE USER HAS CHOSEN TO ENTER AN SUB GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '3'):
            """
            THE USER HAS CHOSEN TO ENTER AN MUL GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '4'):
            """
            THE USER HAS CHOSEN TO ENTER AN DIV GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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
        if(detail == '5'):
            """
            THE USER HAS CHOSEN TO ENTER AN POW GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '6'):
            """
            THE USER HAS CHOSEN TO ENTER AN RAD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

        if(detail == '7'):
            """
            THE USER HAS CHOSEN TO ENTER AN LOG GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                print("The group doesnt exist")
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                print("The group exists")
                is_member = already_In_Group(machine_id, detail)
                if(is_member == True):
                    server_socket.sendto("AM".encode(), client_addr)
                    time.sleep(2)
                    handle_Client(machine_id, client_addr)
                if(is_member == False):
                    server_socket.sendto("NM".encode(), client_addr)
                    confirmation_message, client_addr = server_socket.recvfrom(4096)
                    confirmation_message = confirmation_message.decode()
                    if(confirmation_message == "Proceed"):
                        print("SERVER RECIEVED CONFIRMATION OF GREEN LIGHT TO JOIN")
                        join_Group(machine_id, detail)
                        print("New matrix of groups")
                        print(matrix_of_groups)

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

def remove_Group(machine_id, detail):
    if(detail == '1'):
        """
        WE SHALL DELETE AN ADD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'add'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '2'):
        """
        WE SHALL DELETE AN SUB GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'sub'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '3'):
        """
        WE SHALL DELETE AN MUL GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'mul'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '4'):
        """
        WE SHALL DELETE AN DIV GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'div'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '5'):
        """
        WE SHALL DELETE AN POW GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'pow'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '6'):
        """
        WE SHALL DELETE AN RAD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'rad'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break
    if(detail == '7'):
        """
        WE SHALL DELETE AN LOG GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'log'):
                matrix_of_groups[i][0] = 'empty'
                for j in range(len(matrix_of_groups[i]) - 1):
                    matrix_of_groups[i][j+1] = "nm"
                break

"""
THIS FUCNTIION CORRESPONDS TO THE SECOND OPTION IN THE GROUP MANIPULATION OPTIONS
IT WILL ATEMPT TO ELIMINATE A GROUP
IF IT DOESNT EXISTS IT WILL TELL THE USER
"""
def delete_Group(machine_id, information, client_addr, detail):
    print("The user has elected to delete a group")
    is_already_group = False
    option = True
    while option:
        if(detail == '1'):
            """
            THE USER HAS CHOSEN TO DELETE AN ADD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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
        if(detail == '2'):
            """
            THE USER HAS CHOSEN TO DELETE AN SUB GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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

        if(detail == '3'):
            """
            THE USER HAS CHOSEN TO DELETE AN MUL GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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
        if(detail == '4'):
            """
            THE USER HAS CHOSEN TO DELETE AN DIV GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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

        if(detail == '5'):
            """
            THE USER HAS CHOSEN TO DELETE AN POW GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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
        if(detail == '6'):
            """
            THE USER HAS CHOSEN TO DELETE AN RAD GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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

        if(detail == '7'):
            """
            THE USER HAS CHOSEN TO DELETE AN LOG GROUP
            """
            is_already_group = already_Group(detail)

            if(is_already_group == False):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == True):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    remove_Group(machine_id, detail)
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
THIS FUNCTION WILL CREATE A GROUP AND INSERT THE PERSON WHO CREATED IT TO THE GROUP
EDITORS NOTE: THIS FUNCTION IS READY
"""
def addGroupToMatrix(machine_id, detail):
    print("About to add to matrix")
    print("Detail: ", detail)
    if(detail == '1'):
        """
        WE SHALL CREATE AN ADD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'add'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '2'):
        """
        WE SHALL CREATE A SUB GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'sub'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '3'):
        """
        WE SHALL CREATE A MUL GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'mul'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '4'):
        """
        WE SHALL CREATE A DIV GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'div'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '5'):
        """
        WE SHALL CREATE A POW GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'pow'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '6'):
        """
        WE SHALL CREATE A RAD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if (matrix_of_groups[i][0] == 'empty'):
                matrix_of_groups[i][0] = 'rad'
                matrix_of_groups[i][1] = machine_id
                break
    if(detail == '7'):
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
def already_Group(detail):
    is_already_group = False
    if(detail == '1'):
        """
        USER WANTS TO CREATE AN ADD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'add'):
                is_already_group = True
                break
    if(detail == '2'):
        """
        USER WANTS TO CREATE A SUB GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'sub'):
                is_already_group = True
                break
    if(detail == '3'):
        """
        USER WANTS TO CREATE A MUL GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'mul'):
                is_already_group = True
                break
    if(detail == '4'):
        """
        USER WANTS TO CREATE A DIV GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'div'):
                is_already_group = True
                break
    if(detail == '5'):
        """
        USER WANTS TO CREATE A POW GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'pow'):
                is_already_group = True
                break
    if(detail == '6'):
        """
        USER WANTS TO CREATE A RAD GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'rad'):
                is_already_group = True
                break
    if(detail == '7'):
        """
        USER WANTS TO CREATE A LOG GROUP
        """
        for i in range(len(matrix_of_groups)):
            if(matrix_of_groups[i][0] == 'log'):
                is_already_group = True
                break
    return is_already_group

"""
THIS FUNCTION CORRESPONDS TO THE FIRST OPTION IN THE GROUP MANIPULATION OPTIONS
IT WILL ATEMPT TO CREATE A GROUP
IF IT ALREADY EXISTS IT WILL TELL THE USER
"""
def create_Group(machine_id, information, client_addr, detail):
    print("The user has elected to create a group")
    print("Detailed1: ", detail)
    is_already_group = False
    option = True
    while option:
        print("Detailed1: ", detail)
        if(detail == '1'):
            """
            THE USER HAS CHOSEN TO CREATE AN ADD GROUP
            """
            detail = '1'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '2'):
            """
            THE USER HAS CHOSEN TO CREATE A SUB GROUP
            """
            detail = '2'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '3'):
            """
            THE USER HAS CHOSEN TO CREATE A MUL GROUP
            """
            detail = '3'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '4'):
            """
            THE USER HAS CHOSEN TO CREATE A DIV GROUP
            """
            detail = '4'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '5'):
            """
            THE USER HAS CHOSEN TO CREATE A POW GROUP
            """
            detail = '5'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '6'):
            """
            THE USER HAS CHOSEN TO CREATE A RAD GROUP
            """
            detail = '6'
            is_already_group = already_Group(detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
        if(detail == '7'):
            """
            THE USER HAS CHOSEN TO CREATE A LOG GROUP
            """
            detail = '7'
            print("Detailed3: ", detail)
            is_already_group = already_Group(detail)
            print("Detailed4: ", detail)

            if(is_already_group == True):
                server_socket.sendto("AE".encode(), client_addr)
                time.sleep(2)
                handle_Client(machine_id, client_addr)
            if(is_already_group == False):
                server_socket.sendto("DE".encode(), client_addr)
                confirmation_message, client_addr = server_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == "Proceed"):
                    addGroupToMatrix(machine_id, detail)
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
def group_Manipulation(machine_id, information, client_addr, detail):
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
            THE CLIENT HAS CHOSEN TO CREATE A GROUP
            EDITORS NOTE: READY
            """
            create_Group(machine_id, information, client_addr, detail)
        if(information == '2'):
            """
            THE CLIENT HAS CHOSEN TO DELETE A GROUP
            EDITORS NOTE: READY
            """
            delete_Group(machine_id, information, client_addr, detail)
        if(information == '3'):
            """
            THE CLIENT HAS CHOSEN TO ENTER A GROUP
            EDITORS NOTE: READY
            """
            enter_Group(machine_id, information, client_addr, detail)
        if(information == '4'):
            """
            THE CLIENT HAS CHOSEN TO EXIT A GROUP
            EDITORS NOTE: NONE EXISTENT
            """
            exit_Group(machine_id, information, client_addr, detail)
        if(information == '5'):
            """
            THE CLIENT HAS CHOSEN TO SHOW ALL GROUP
            EDITORS NOTE: NONE EXISTENT
            """
            create_Group(machine_id, information, client_addr, detail)
        if(information == '6'):
            """
            THE CLIENT HAS CHOSEN TO SEND MESSAGE TO A GROUP
            EDITORS NOTE: NONE EXISTENT
            """
            create_Group(machine_id, information, client_addr, detail)
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
            detail =array_data[3]
            print("Machine id: ", machine_id)
            print("Operation: ", operation)
            print("Information: ", information)
            print("Detail", detail)
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
                print("Successfully retrieved the data from the client")
                """
                OPERATION
                1 MEANS GROUP MATRIX MANIPULATION
                """
                if(operation == '1'):
                    print("We know what the client wants")
                    group_Manipulation(machine_id, information, client_addr, detail)



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
