#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16CSE037
#
# Created:     21/10/2017
# Copyright:   (c) 16CSE037 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    stringVar = "programmer"
    loc = stringVar.count('a')
    print (loc)
    loc = stringVar.find('g')
    print (loc)
    stringVar = stringVar.lower()
    print (stringVar)
    stringVar = stringVar.upper()
    print (stringVar)
    stringVar = stringVar.replace('a', 'f')
    print (stringVar)
    stringVar = stringVar.strip()
    print (stringVar)
    print(len(stringVar))

if __name__ == '__main__':
    main()
