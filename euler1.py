#Find the sum of all the multiples of 3 or 5 below a limit defined by user
# % is the modulus operator

def sum_3_5(limit):
    sum = 0
    for x in range(1, limit):
        if x % 3 == 0:
            sum += x 
        elif x % 5 == 0:
            sum += x 
    return sum

limit = input('What is the limit? ')
limit = int(limit)
sum = sum_3_5(limit)

print('\n\n{}\n\n\n'.format(sum))

assert sum == 233168