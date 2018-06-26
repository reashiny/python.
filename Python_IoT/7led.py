import RPi.GPIO as GPIO
import time
import sys
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
def pin_configure():
    for i in pins:
        GPIO.setup(i,GPIO.OUT)
def pin_initiate():
    for i in pins:
        GPIO.output(i,0)
pin_configure()
def display(out):
    pin_initiate()
    for i in out:
        GPIO.output(i,1)
        print("{} PIN ON".format(i))
def assign(a):
    if(a==0):
        display(zero)
    if a==1:
        display(one)
        print("one")
    if(a==2):
        display(two)
    if(a==3):
      display(three)
    if(a==4):
      display(four)
     
    if(a==5):
      display(five)
    
    if(a==6):
     display(six)
    if(a==7):
     display(seven)
    if(a==8):
       display(eight)
    if(a==9):
        display(nine)
while 1:
    a=int(input("enter the number"))
    assign(a)



 
    

