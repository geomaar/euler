import math

def is_square(n): 
    if n< 0:
        return False 
    else:
        if int(math.sqrt(n) + 0.5) ** 2 == n:
            return True
        else:
            return False


'''
import math

def is_square(n):    

    if n < 0:
        return False

    sqrt = math.sqrt(n)
    
    return sqrt.is_integer()
'''