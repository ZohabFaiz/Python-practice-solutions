#print number in a pattern

n=int(input('enter a number :'))

for i in range(0,n):
    
    for j in range(0,n):

        if i>=j:
            print(j+1, end=' ')


    print()

    