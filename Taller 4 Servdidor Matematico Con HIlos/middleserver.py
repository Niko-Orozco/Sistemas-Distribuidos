import zmq
import json
import socket

"""This is the TCP protocol"""
context = zmq.Context()
middle_Server_Socket = context.socket(zmq.REQ)
print("Middle Server socekt connected")
middle_Server_Socket.connect("tcp://127.0.0.1:5555")

"""This is for the UDP protocols"""
middle_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Middle Server socekt connected")
host = 'localhost'
port = 5432

middle_Socket.bind((host,port))
print("Middle server UDP socket conecter to", host)


"""DEFAULT MESSAGE"""
confirmation_Message = "Data recieved in middelserver"

while True: 
    data, addr = middle_Socket.recvfrom(4096)
    if  data: 
        print(confirmation_Message)
        data = json.loads(data.decode())
        array_Data = data.get("data")
        option = array_Data[0]
        number_Array = array_Data[1]
        print(number_Array)
        try:
            "Sending the json to the server where the calculation will occur"
            print("Sending data to server for addition")
            middle_Server_Socket.send_json(data)
            print("Data sent")
            "Recieving response from server"
            print("Recieving response from server")
            result = middle_Server_Socket.recv_string()
            if result:
                print(confirmation_Message)
                print("Sending result to client")
                middle_Socket.sendto(result.encode(), addr)
        except Exception as e:
            print(e)
