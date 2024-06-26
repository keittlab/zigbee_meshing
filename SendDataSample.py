# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = "Hello XBee!"
REMOTE_NODE_ID = "END_DEVICE"
FILE_TO_SEND = "/home/mesh3/dev/zigbee_meshing/files/send.txt"

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
        
def main():
    print(" +--------------------------------------+")
    print(" | XBee Python Library Send Data Sample |")
    print(" +--------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        content = read_file(FILE_TO_SEND)

        DATA_TO_SEND = content

        # Get the XBee network object from the local XBee.
        xnet = device.get_network()
                
        # Start the discovery process and wait for it to be over.
        xnet.start_discovery_process(deep=True, n_deep_scans=1)
        while xnet.is_discovery_running():
            time.sleep(0.5)
                
        # Get the list of the nodes in the network.
        nodes = xnet.get_devices()
    
        # Print the output log discovered local nodes.
        remote_device = None
        print("Discovered local nodes:")
        for node in nodes:
            remote_device = node
            print(" - %s" % remote_device)

        # remote_device = xnet.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)

        print("Sending data to %s >> %s..." % (node.get_64bit_addr(), DATA_TO_SEND))

        device.send_data(remote_device, DATA_TO_SEND)

        print("Success")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
