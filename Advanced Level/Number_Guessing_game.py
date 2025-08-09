#number guessing game

import random

x= random.randint(1,100)

count=0
while True:
    y= int(input('Enter your guess: '))
    count=count+1
    if y>x:
        if y-x>5:
        
         print('Guess Too High ')

        else : print('Guess is High')

    if y<x:
        if x-y>5:
        
         print('Guess Too Low ')

        else : print('Guess is Low')

    if y==x :
        print('Right Guess in : ',count,' chance')
        break
