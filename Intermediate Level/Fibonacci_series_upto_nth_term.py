# print fibonacci serese for first n numbers


n= int(input('Enter the number of terms to print : '))


x=[0,1]
series=0
if n>0 :
    for i in range(0,int(n)):
        
        series=x[i]+x[i+1]
        x.append(series)

        print(x[i],end=' ')
        