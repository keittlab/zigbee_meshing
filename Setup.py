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

device = XBeeDevice("/dev/ttyUSB0", 9600)  
# NOTE: Change "/dev/ttyUSB0" to the according serial port
# that the XBee is plugged into.

# dmesg | grep tty
# This is the command to find what port the RPi is in
# Ex: "now attached to ttyUSB0"

try:
    device.open()
    # Open device connection.
        
    # Get the XBee network object from the local XBee.
    xnet = device.get_network()
            
    # Start the discovery process and wait for it to be over.
    xnet.start_discovery_process(deep=True, n_deep_scans=1)
    while xnet.is_discovery_running():
        time.sleep(0.5)
            
    # Get the list of the nodes in the network.
    nodes = xnet.get_devices()

    # Print the output log discovered local nodes.
    print("Discovered local nodes:")
    for node in nodes:
        print(" - %s" % node)

finally:
    if device is not None and device.is_open():
        device.close()