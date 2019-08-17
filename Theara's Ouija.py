from string import ascii_lowercase
import itertools
ouija=[]
a=int(input())
for i,c in zip(range(1,27),ascii_lowercase):
    if len(ouija)==a:
        break
    for j in range (1,i+1):
        ouija.append(i)
        if len(ouija)==a:
            break
    for k in range (1,i+1):
        ouija.append(c)
        if len(ouija)==a:
            break   
print(ouija[a-1])

    