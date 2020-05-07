""" 
Mastermind quarantine edition
Four letters: a, b, c, d in a random order
User should find correct combination in 10 tries
After each try, user will get: X correct X wrong
"""
import random

balls = ['a', 'b', 'c', 'd']
comb= [random.choice(balls), random.choice(balls), random.choice(balls), random.choice(balls)]
#print(comb)
print('Welcome! Find the combination, there are four letters in the combination: a, b, c, d')

for j in range (10):
    right = 0
    wrong = 0
    guess = input("Enter your combination separated by space: ").split()
    for i in range (4):
        if guess[i] == comb[i]:
            right+= 1
        else:
            wrong+= 1
    if right == 4:
            print('You won!')
            break
    else:
        print('Right=',right, 'Wrong=', wrong, 'Guess= ', j+1)
    if j == 9:
        print('You lost, the correct combination is:', comb)