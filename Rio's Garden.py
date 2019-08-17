import numpy as np 
n=int(input())
arr=np.zeros((n,n))
for i in range(n):
    line_input=input()
    k=0
    for j in line_input.split():
            arr[i,k]=int(j)
            k+=1
a=int(input())
for i in range(0,n,a):
    for j in range(0,n,a):
         y=arr[i:i+a,j:j+a]
         avg=int(np.sum(y)//(a*a))
         b=np.array([avg]*(a*a),dtype=int)
         b=b.reshape(a,a)
         arr[i:i+a,j:j+a]=b
print(int((n/a)*(n/a)))
print (arr)

          

        
