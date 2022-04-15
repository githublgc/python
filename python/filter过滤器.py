#!/usr/bin/python3
def is_odd(n):
    if n==192:
       return n  
t = filter(is_odd, [192,127,168])
n = list(t)
print(n)
