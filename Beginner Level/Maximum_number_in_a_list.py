#finding maximun in a list


x=[21,3243,4,55,98,32]

maximum=0

for i in range(0,len(x)):

    if x[i]>=maximum:
        maximum=x[i]
    else: continue


print(maximum)
