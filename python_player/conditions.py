#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      16cse037
#
# Created:     21/10/2017
# Copyright:   (c) 16cse037 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
n = 3
if False:
    n += 2
n += 3
if True:
    n += 4
print(n)

