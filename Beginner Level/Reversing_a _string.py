#Reversing a string

user_input=input('Enter a string :')


for i in range(len(user_input)):
    print(user_input[len(user_input)-1-i], end='')