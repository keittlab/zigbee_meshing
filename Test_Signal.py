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

# Again, instantiate the coordinator XBee object.
device = XBeeDevice("/dev/ttyUSB0", 9600)  
# NOTE: Change "/dev/ttyUSB0" to the according serial port
# that the XBee is plugged into.

# dmesg | grep tty
# This is the command to find what port the RPi is in
# Ex: "now attached to ttyUSB0"

try:
    # Open the device connection.
    device.open()

    # Grabbing the address of all the nodes in the network.
	network = device.get_network()
    nodes = network.get_devices()

    # Send a data frame to each node and read the signal strength of the response.
    for node in nodes:
        transmit_status = device.send_data_async(node, "test")
        print("Signal strength to node %s: %d" % (node.get_64bit_addr(), transmit_status.transmit_status.retries))

finally:
		# Close the device connection.
    if device is not None and device.is_open():
        device.close()