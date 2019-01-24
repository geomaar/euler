"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
a=2**1000
print(a)
a_str=str(a)
b=0
for num in range(0, len(a_str)):
    b=b+int(a_str[num])
print(b)
