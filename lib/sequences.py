#!/usr/bin/env python3

def print_fibonacci(length):

    if length == 0:
       print([])
    elif length == 1:
       print([0])
    else:    
        fibo = [0]*length
        fibo[0] = 0
        fibo[1] = 1

        for i in range(2,length):
            fibo[i] = fibo[i-1] + fibo[i-2]

        print(fibo)




    pass