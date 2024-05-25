# Update Raspberry Pi's internal time with the web
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

os.system('sudo service ntp stop')
os.system('sudo ntpd -q -g')
os.system('sudo service ntp start')

# Synchronize times with other Raspberry Pis through XBee
ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(ser)

while True:
    try:
        # Send the current time to other Raspberry Pis
        xbee.tx(dest_addr=b'\x00\x01', data=str(time.time()))
        time.sleep(1)
    except KeyboardInterrupt:
        break

ser.close()
