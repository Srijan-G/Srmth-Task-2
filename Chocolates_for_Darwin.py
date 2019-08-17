import math
def factorial(a):
    flag=1
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            flag=0
            break
    if a==2 :
      flag=1
    if flag==1:
        return True
    else:
        return False

def main():
    a=int(input())
    total=0
    i=a-1
    while i>=2:
        if a==0:
            break
        if factorial(i) and a-i>=0 and a-i!=1:
            total+=1
            a=a-i 
            i+=1
        i-=1   
    print (total)

if __name__=="__main__":
    main()