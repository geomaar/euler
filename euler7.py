"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

target = 600851475143 

def is_prime(x, primes):
    for p in primes:
        if p >= x:
            break
        if x % p == 0:
            return False

    return True

primes=[2] 
for n in range(3,math.ceil(math.sqrt(target)),2):
    if n%10000==1:
        print('Hold on! I am on' , n)
    if is_prime(n,primes):
        primes.append(n)
        if len(primes)>10001:
            break

print(primes[10000])