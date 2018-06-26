#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      16cse037
#
# Created:     25/06/2018
# Copyright:   (c) 16cse037 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
fib=[]
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    fib.append(fibonacci(i))
for i in fib:
    print(i)