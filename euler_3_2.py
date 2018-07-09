from itertools import takewhile
import math

def is_prime(x, primes):
    for p in primes:
        if p >= x:
            break

        if x % p == 0:
            return False

    return True

# print(is_prime(10, [2, 3, 5, 7]))

def primes_up_to(n):
    primes = [2]

    for x in range(3, n+1):
        if is_prime(x, primes):
            primes.append(x)

    return primes

# print(primes_up_to(20))

def prime_factors(n):
    primes = primes_up_to(n)
    factors = [] 
    for prime in primes:
        if prime >= n:
            break

        if n % prime == 0:
            factors.append(prime)
    return factors

print(prime_factors(13195))