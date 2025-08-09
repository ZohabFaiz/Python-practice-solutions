#reverse a list

x=[1,2,3,4,5]
y=[]

for i in range(0,len(x)):

    y.append(x[len(x)-i-1])


print(y)
    