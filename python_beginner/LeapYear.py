#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16cse037
#
# Created:     03/09/2018
# Copyright:   (c) 16cse037 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    year=input("Enter the year")
    if(year%400==0):
        print(year,"is leap year")
    elif(year%100==0):
        print(year,"isn't leap year")
    elif(year%4==0):
        print(year,"is leap year")
    else:
        print(year,"isn't leap year")


if __name__ == '__main__':
    main()
