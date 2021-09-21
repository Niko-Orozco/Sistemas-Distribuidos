import zmq



context = zmq.Context()
socket = context.socket(zmq.REP)
print('Server socket created')
socket.bind("tcp://*:5555")
print('Server socket conected to localhost')

while True:
    """ Recieves Number 1 and sends confirmation TCP"""
    number1 = socket.recv()
    if number1:
        number1 = number1.decode()
        print('From client: ', number1)
        socket.send_string(number1)
        print('Sending ', number1)
        print('')
    """ Recieves Number 2 and sends confirmation TCP"""
    number2 = socket.recv()
    if number2:
        number2 = number2.decode()
        print('From client: ', number2)
        socket.send_string(number2)
        print('Sending ', number2)
        print('')
    result = socket.recv()
    if number1 and number2:
        num1 = (int(number1))
        num2 = (int(number2))
        result = num1 + num2
        res = (str(result))
        print('Sending ', res)
        socket.send_string(res)
