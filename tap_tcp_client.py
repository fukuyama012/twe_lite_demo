# -*- coding: utf-8 -*- 
# TWE LITE 2525A Demonstration Client
# * you have to prepare server system
#
# Source available at https://github.com/fukuyama012/twe_lite_demo
# This is distributed under the terms of the MIT license.

import serial
import socket
from contextlib import closing

# SERIAL INTERFACE INFO
SERIAL_BITRATE = 115200
SERIAL_PORT    = 2

# SEVER INFO
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 11000


def is_tap_action(data):
    """
    confirmation of data whether format is tap action
    
    :param data: string data received from serial
    :return: tap action or not
    """
    m = str(data).split(";")
    if len(m) == 16 and int(m[7]) == 1:
        return True
    else:
        return False


def main():
    """main"""
    tap = "tap"# signal to sever
    
    s = serial.Serial(SERIAL_PORT, SERIAL_BITRATE)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(client):
        client.connect((SERVER_HOST, SERVER_PORT))
        while True:
            data = s.readline()
            if is_tap_action(data) == True:
                client.send(tap.encode('utf-8'))
                #print("tap")
    return


if __name__ == "__main__":
    main()