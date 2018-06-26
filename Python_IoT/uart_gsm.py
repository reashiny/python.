import serial
import time

uart = serial.Serial("/dev/ttyS0",9600)

Ph_No = ""

def Send_Message(msg):
    uart.write("AT\r\n")
    print("AT\r\n")
    time.sleep(.5)

    uart.write("AT+CMGF=1\r\n")
    print("AT+CMGF=1\r\n")
    time.sleep(.5)

    uart.write("AT+CMGS="+Ph_No+"\r\n")
    print("AT+CMGS="+Ph_No+"\r\n")
    time.sleep(.5)

    uart.write(msg)
    print(msg)
    uart.write("\x1A")
    time.sleep(.5)

while True:
    m = input("Enter MEssage:")
    Send_Message(m)
    time.sleep(2)
