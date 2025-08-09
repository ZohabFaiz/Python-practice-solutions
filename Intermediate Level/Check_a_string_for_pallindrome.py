#check if a string is pallindrome or not


x= input('Enter a string: ')

y=[]


for i in range(0, len(x)):

    y.append(x[-i-1])

    if y[i]==x[i]:

        if i==len(x)-1:
            print('Pallindrome')

        continue


    else:
        print('not pallindrome')
        break
        

