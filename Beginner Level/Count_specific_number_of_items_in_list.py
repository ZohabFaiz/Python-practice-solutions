#Count how many specific items appear in a list

x=['money','ajay','figure','ajay','ajay','hello','figure','ajay','hello','ajay']

ajay=0

for i in x:
    if i=='ajay':
        ajay= ajay+1
    else: continue

print(ajay)
        