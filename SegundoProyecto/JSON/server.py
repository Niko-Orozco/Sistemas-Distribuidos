import zmq
import json
import math



context = zmq.Context()
socket = context.socket(zmq.REP)
print('Server socket created')
socket.bind("tcp://*:5555")
print('Server socket conected to localhost')

"""Default Messages"""
confirmationMessage = 'Data recieved in server'

while True:
    data = socket.recv_json()
    print(data)
    if data:
        jsondata = json.loads(data)
        arrayData = jsondata.get("data")
        option = arrayData[0]
        number1 = arrayData[1]
        number2 = arrayData[2]
        try:
            """TCP"""
            print('Data recieved succesfully')
            socket.send_string(confirmationMessage)
        except Exception as e:
            print(e)
        res = socket.recv()
        if option == 'a':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = num1 + num2
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
        elif option == 's':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = num1 - num2
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
        elif option == 'm':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = num1 * num2
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
        elif option == 'd':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = num1 / num2
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
        elif option == 'p':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = pow(num1, num2)
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
        elif option == 'l':
            try:
                num1 = (float(number1))
                num2 = (float(number2))
                result = math.log(num2, num1)
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
