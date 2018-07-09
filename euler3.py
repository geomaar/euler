# The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Define list of prime numbers

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

print(primes)

list=[]          
for k in primes:
    if k%10000==0:
        print(k)
    if target % k == 0:
        list.append(k)

print(list[-1])
