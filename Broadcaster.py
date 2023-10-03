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

# Instantiate the boardcasting XBee device object.
device = XBeeDevice("COM1", 9600)  # NOTE: Change "COM1" to the according serial port
# that the XBee is plugged into. COM1 is placed here as a placeholder assuming the
# XBee device is plugged into "USB-A Port 1".

try:
	# Open the device.
	device.open()
	
	device.send_data_broadcast("Test Thingity Test!")
	# Broadcast the test signal.

finally:
		# Close the device connection.
    if device is not None and device.is_open():
        device.close()

        