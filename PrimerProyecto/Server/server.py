import zmq



context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    msg = socket.recv()
    print('From client: ', msg)
    smsg = input('Enter your msg here: ')
    socket.send_string(smsg)
    print('')
