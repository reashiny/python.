#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shiny
#
# Created:     03/03/2018
# Copyright:   (c) Shiny 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a=raw_input("enter the value")
b=raw_input("enter the value")
c=raw_input("enter the value")
if(a>b and a>c):
    print (a,"is greater")
elif(b>c):
    print(b,"is greater")
else:
    print(c,"is greater")