#!/usr/bin/python3

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5556")

while True:
    msg = socket.recv()
    print(msg)
