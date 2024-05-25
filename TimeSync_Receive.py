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