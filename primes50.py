# The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

#Define list of prime numbers

import math

prime=[]


for i in range(1, 50):
    count=0
    for j in range(1,i+1):
        if i % j== 0:
            count += 1
    if count <= 2:
        prime.append(i)
print(prime)

list=[]          
for k in prime:
    if 13195 % k == 0:
        list.append(k)

print(list)
