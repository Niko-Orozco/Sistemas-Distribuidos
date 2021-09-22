import zmq
import json



context = zmq.Context()
socket = context.socket(zmq.REP)
print('Server socket created')
socket.bind("tcp://*:5555")
print('Server socket conected to localhost')

"""Default Messages"""
confirmationMessage = 'Data recieved in server'

while True:
    data = socket.recv_json()
    if data:
        """data = json.loads(data.decode())"""
        arrayData = data.get("data")
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
                num1 = (int(number1))
                num2 = (int(number2))
                result = num1 + num2
                res = (str(result))
                print('Sending ', res)
                socket.send_string(res)
            except Exception as e:
                print(e)
