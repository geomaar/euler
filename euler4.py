#A palindromic number reads the same both ways. The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#Test case, just to verify my result is correct (which it is)
for i in range(10,100):
    for j in range(10,100):
        pal=i*j
        x=str(pal)
        if x==x[::-1]:
            print(pal, i, j)


product=[]
for i in range(100,1000):
    for j in range(100,1000):
        pal=i*j
        x=str(pal)
        if x==x[::-1]:
            #print(pal, i, j)
            product.append(pal)

print(max(product))

