# Update Raspberry Pi's internal time with the web
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