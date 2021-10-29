import zmq 
import json
import math


context = zmq.Context()
server_Socket = context.socket(zmq.REP)
print("Server socket connected")
server_Socket.bind("tcp://*:5555")
print("Server socket connected to local host")

"""Default Messages"""
confirmation_Message = "Data recieved in server"

while True:
    data = server_Socket.recv_json()
    if data:
        print(confirmation_Message)
        array_Data = data.get("data")
        option = array_Data[0]
        number_Array = array_Data[1]
        number_Quantity = len(number_Array)
        sum_Total = 0
        if option == "a":
            try:
                for i in range(number_Quantity):
                    sum_Total += int(number_Array[i])
                result = str(sum_Total)
                print("Sending result to middleserver: ", result)
                server_Socket.send_string(result)
            except Exception as e:
                print(e)