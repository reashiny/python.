import serial


uart = serial.Serial("/dev/ttyS0",9600)


while True:
    received_data = uart.inWaiting()
    if received_data != 0:
	print(uart.read(received_data))
	
