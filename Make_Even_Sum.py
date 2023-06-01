n=int(input())
a=list(map(int,input().split()))
c=0
d=sum(a)
if(d%2==0):
    c+=1
print(c)