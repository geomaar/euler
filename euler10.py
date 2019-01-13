"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math 

target = 2000000
def is_prime(x, primes):
    for p in primes:
        if p >= x:
            break
        if x % p == 0:
            return False

    return True

primes=[2] 
for n in range(3,target,2):
    if n%10000==1:
        print('Hold on! I am on' , n)
    if is_prime(n,primes):
        primes.append(n)


print(primes)
print(sum(primes))