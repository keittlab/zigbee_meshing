from digi import xbee
from digi.xbee.devices import DigiMeshDevice
from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.models.mode import NeighborDiscoveryMode
import time


def main():

    device = DigiMeshDevice("/dev/ttyUSB0", 9600)

    device.open()

    xbee_network = device.get_network()
    xbee_network.set_deep_discovery_options(NeighborDiscoveryMode.CASCADE)
    xbee_network.set_deep_discovery_timeouts(15)
    xbee_network.clear()

    # Callback for discovered devices.
    def callback_device_discovered(remote):
        print("Device discovered: %s" % remote)

    # Callback for discovery finished.
    def callback_discovery_finished(status):
        if status == NetworkDiscoveryStatus.SUCCESS:
            print("Discovery process finished successfully.")
            if xbee_network.has_devices():
                print("%s" % '\n    '.join(map(str, xbee_network.get_connections())))          

            xbee_network.start_discovery_process(deep=True)      

        else:
            print("There was an error discovering devices: %s" % status.description)

    xbee_network.add_device_discovered_callback(callback_device_discovered)
    xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

    xbee_network.start_discovery_process(deep=True)

    while 1:
        print("discovery running:"+str(xbee_network.is_discovery_running()))
        time.sleep(1)   

    devices_found = xbee_network.get_devices()
    for found_dev in devices_found:
        print()

    if device is not None and device.is_open():
        device.close()    

if __name__ == '__main__':
    main()
