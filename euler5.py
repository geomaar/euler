"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Just using math it would be 16*9*5*7*11*13*17*19= 232792560

from functools import reduce
import math 


def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//math.gcd(a,b)
    
# Test with initial data to compare final result
a=reduce(lcm, range(1,10+1))
print(a)

b=reduce(lcm, range(1,20+1))
print(b)