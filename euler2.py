# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

#Fibonacci
fib = [1,2]
for x in range (2,50):
    fib.append(fib[x-1]+fib[x-2])
#print(fib[-1]) #-1 indicates the last value of a list

sum = 0

for i in fib:
    if i<= 4000000 and i % 2 == 0:
        sum += i

print(sum)