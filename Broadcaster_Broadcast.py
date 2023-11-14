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

device = XBeeDevice("/dev/ttyUSB0", 9600)  
# NOTE: Change "/dev/ttyUSB0" to the according serial port
# that the XBee is plugged into.

# dmesg | grep tty
# This is the command to find what port the RPi is in
# Ex: "now attached to ttyUSB0"

try:
	# Open the device.
	device.open()
	
	# Broadcast the test signal
	device.send_data_broadcast("Test Thingity Test!")

finally:
		# Close the device connection.
    if device is not None and device.is_open():
        device.close()

        