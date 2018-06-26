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

    print(data)

    return data

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.OUT)

GPIO.output(10,False)


url = "http://www.azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00050"


while True:

    value = read_data_base(url)

    if value == b'1':

        GPIO.output(10,True)
        print("ON")
        time.sleep(0.5)
        GPIO.output(10,False)
        time.sleep(0.005)
        

    else:

        GPIO.output(10,False)
        print("off")











