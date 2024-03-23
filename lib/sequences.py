#!/usr/bin/env python3

def print_fibonacci(length):
    small_fib = [0,1,1,2,3,5,8,13,21]
    if length > 9:
        while len(small_fib) < length:
            new_num = small_fib[-2] + small_fib[-1]
            small_fib.append(new_num)
        return print(small_fib[0:length])
    else:
        return print(small_fib[0:length])
