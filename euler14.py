"""
The following iterative sequence is defined for the set of positive integers:

n - n/2 (n is even)
n - 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

note: Once the chain starts the terms are allowed to go above one million.
"""


def func(x):
    while True:
        yield x
        if x == 1:
            break
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x+1
    return

# Test with data from problem
# print(list(func(13)))

a=[]
for num in range(1,1000000):
    a.append((len(list(func(num))),num))
    
print(max(a))

