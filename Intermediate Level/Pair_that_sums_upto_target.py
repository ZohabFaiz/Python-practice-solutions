# print the pair that sums up to target


x = [1, 2, 3, 4, 5] 
Target = 6  
pair=[]
for i in range(0,len(x)):
    for j in range(0,len(x)):
        if i!=j:
            if j >i:
                if x[i]+x[j]==6:
                    pair.append((x[i],x[j]))
            else: continue



print(pair)                
