def likes(names):
    if len(names) == 0:  
        return 'no one likes this'

    if len(names) == 1:
        return names[0] + ' likes this'
    
    result = names[-1] + ' like this'

    if len(names) > 1 and len(names)< 4:
        prefix = ', '.join(names[:-1])
        result = prefix + ' and ' + result
        return result

    if len(names) >= 4:
        return names[0] + ', ' + names[1] + ' and '+ str(len(names)- 2) + ' others like this'

'''
Solution provided by Codewars:
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)
'''