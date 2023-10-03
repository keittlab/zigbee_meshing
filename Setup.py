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
from ipadress import IPv4Address
from queue import Queue, Empty
from digi.xbee.serial import FlowControl, XBeeSerialPort

device = XBeeDevice("COM1", 9600)  # NOTE: Change "COM1" to the according serial port
# that the XBee is plugged into. COM1 is placed here as a placeholder assuming the
# XBee device is plugged into "USB-A Port 1".

try:

    device.open()
		# Open device connection.


    local = device.get_local_xbee_device()
    # Obtain the local nodes.

    print("Discovered local nodes:")
    for node in local:
        print(" - %s" % node)
    # Print the output log discovered local nodes.

    local_add = local.get_64bit_addr()
    # Obtain the MAC Address of the local node.

    print("Discovered local node addresses:")
    for addr in local_add:
        print(" - %s" % addr)
    # Print the output log discovered local nodes.

    remote = device.get_network().discover_devices()


    # Print the output log discovered remote nodes.
    print("Discovered remote nodes:")
    for node in remote:
        print(" - %s" % node)

finally:
    if device is not None and device.is_open():
        device.close()