import serial
import time

s1=serial.Serial('/dev/ttyS0',9600)

def send_msg():
    s1.write("hai")
    print("hai")
def read_msg():
    k=s1.readline()
    time.sleep(2)
    print(k)
send_msg()
while 1:
    read_msg()
