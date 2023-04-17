r,c=map(int,input().split())
mat=[]
d=0
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
for j in mat:
    d+=sum(j)
    
print(d)