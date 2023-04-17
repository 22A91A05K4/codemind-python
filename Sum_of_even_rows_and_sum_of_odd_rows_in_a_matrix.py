r,c=map(int,input().split())
mat=[]
d=0
e=0
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
for i in range(r):
    if i%2==0:
        d+=sum(mat[i])
    else:
        e+=sum(mat[i])
print(d,e,end=' ')
