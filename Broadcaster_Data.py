import numpy as np
import os
import datetime
import time
import serial
from digi.xbee.devicese import XBeeDevice
from xbee import XBee
from digi.xbee import serial
from digi.xbee.util import utils
from abc import ABCMeta, abstractmethod
from enum import enum, unique
from functools import wraps
from ipadress import IPv4Address
from queue import Queue, Empty
from digi.xbee.serial import FlowControl, XBeeSerialPort

# Replace with the path to the directory containing the files to send
dir_path = '/path/to/directory'

def send_file(xbee, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        xbee.tx(dest_addr='\x00\x01', data=data)

def main():
    ser = serial.Serial("/dev/ttyUSB0", 9600) 
    # NOTE: Change "/dev/ttyUSB0" to the according serial port
    # that the XBee is plugged into.

    # dmesg | grep tty
    # This is the command to find what port the RPi is in
    # Ex: "now attached to ttyUSB0"

    xbee = XBee(ser)

    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            send_file(xbee, file_path)

    ser.close()

if __name__ == '__main__':
    main()