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
a=raw_input("enter any chracter")
if((a>='a' and a<='z') or (a>='A' and a<='Z')):
    print (a, "is an alphabet")
else:
    print(a ,"is not an alphabet")