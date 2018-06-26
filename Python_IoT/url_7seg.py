import RPi.GPIO as GPIO
import time

import urllib3


def write_data_base(url,data):

    http = urllib3.connection_from_url(url)

    r = http.urlopen('SET',url+str(data))

def read_data_base(url):

    http = urllib3.connection_from_url(url)

    r = http.urlopen('GET',url)

    data = r.data.decode("utf-8-sig").encode("utf-8")
    return data

GPIO.setmode(GPIO.BOARD)
pins=[3,5,7,11,13,15,19]
zero=[3,5,7,11,13,15]
one=[5,7]
two=[3,5,11,19,13]
three=[3,5,7,11,19]
four=[5,7,19,15]
five=[3,7,11,15,19]
six=[3,7,11,13,15,19]
seven=[3,5,7]
eight=[3,5,7,11,13,15,19]
nine=[3,5,7,11,15,19]
GPIO.setwarnings(False)


url = "http://www.azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00050"

for i in pins:
        GPIO.setup(i,GPIO.OUT)
def pin_initiate():
    for i in pins:
        GPIO.output(i,0)
def display(out):
    pin_initiate()
    for i in out:
        GPIO.output(i,1)
        print("{} PIN ON".format(i))
def assign():
     while True:
        value = read_data_base(url)
        print(value)
        if value == b'0':
            display(zero)
        if value == b'1':
            display(one)
        if value == b'2':
            display(two)
        if value == b'3':
          display(three)
        if value == b'4':
          display(four)
        if value == b'5':
          display(five)
        if value == b'6':
         display(six)
        if value == b'7':
         display(seven)
        if value == b'8':
           display(eight)
        if value == b'9':
            display(nine)
while 1:
    assign()

   
