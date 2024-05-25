import numpy as np
import os
import datetime
import time
import serial
from digi.xbee.devices import XBeeDevice
from xbee import XBee
from digi.xbee import serial
from digi.xbee.util import utils
from abc import ABCMeta, abstractmethod
# from enum import enum, unique
from functools import wraps
from ipaddress import IPv4Address
from queue import Queue, Empty
from digi.xbee.serial import FlowControl, XBeeSerialPort

def update_time(data):
    # Update Raspberry Pi's internal time with received time
    os.system(f'sudo date -s @{data["rf_data"].decode()}')

# Receive current time from other Raspberry Pi through XBee
ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(ser, callback=update_time)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

ser.close()
