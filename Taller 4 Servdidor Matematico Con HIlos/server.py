import zmq 
import json
import math
import queue
import concurrent.futures

context = zmq.Context()
server_Socket = context.socket(zmq.REP)
print("Server socket connected")
server_Socket.bind("tcp://*:5555")
print("Server socket connected to local host")

"""Default Messages"""
confirmation_Message = "Data recieved in server"

def parallelSum(number_Array):
    print("ENTRERING PARALELISM")
    que1 = queue.Queue()
    que2 = queue.Queue()
    half = len(number_Array)//2
    length = len(number_Array)
    first_Half = []
    second_Half = []
    result = 0
    for i in range(half):
        first_Half.append(number_Array[i])
    for i in range(half, length):
        second_Half.append(number_Array[i])
    'ADDING BOTH HALFS'
    print("SUCCESSFULLY DIVIDED ARRAYS")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        first_Half_Result = executor.submit(addingHalf, first_Half)
        second_Half_Result = executor.submit(addingHalf, second_Half)

        first_Half_Return_Value = first_Half_Result.result()
        second_Half_Return_Value = second_Half_Result.result()

        print(first_Half_Return_Value)
        print(second_Half_Return_Value)

        result = int(first_Half_Return_Value) + int(second_Half_Return_Value)
    return result
    
    

def addingHalf(half_Array):
    length = len(half_Array)
    half_Result = 0
    for i in range(length):
        half_Result += int(half_Array[i])
    return half_Result


while True:
    data = server_Socket.recv_json()
    if data:
        print(confirmation_Message)
        array_Data = data.get("data")
        option = array_Data[0]
        number_Array = array_Data[1]
        sum_Total = 0
        if option == "a":
            try:
                'Parallel'
                sum_Total = parallelSum(number_Array)
                result = str(sum_Total)
                print("Sending result to middleserver: ", result)
                server_Socket.send_string(result)
            except Exception as e:
                print(e)
        if option == "s":
            try:
                'Parallel'
            except Exception as e:
                print(e)
