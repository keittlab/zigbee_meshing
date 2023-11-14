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

dir_path = '/path/to/directory'

def save_file(data):
    file_path = os.path.join(dir_path, 'received_file')
    with open(file_path, 'wb') as file:
        file.write(data)

def main():
    ser = serial.Serial("/dev/ttyUSB0", 9600) 
    # NOTE: Change "/dev/ttyUSB0" to the according serial port
    # that the XBee is plugged into.

    # dmesg | grep tty
    # This is the command to find what port the RPi is in
    # Ex: "now attached to ttyUSB0"
    
    xbee = XBee(ser)

    while True:
        try:
            response = xbee.wait_read_frame()
            save_file(response['rf_data'])
        except KeyboardInterrupt:
            break

    ser.close()

if __name__ == '__main__':
    main()