# factorial.py 

import time
import sys
final_list = [] 

def factorial(n):

    time.sleep(.1)

    factorial = 1

    for i in range (1,n+1):

        factorial = factorial * i

    return factorial  

def sum_factorial(num):  

    for i in range(num):

        final_list.append(factorial(i)) 

    result=sum(final_list) 

    print("Final SUM is {}".format(result))
    print("THis is the new latest change")

    return result

if __name__ == "__main__": 
    if sys.argv[1] != None:
        sum_factorial(int(sys.argv[1]))
    else :
         sum_factorial(50)