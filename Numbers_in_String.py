s=input()
c=0
for i in s:
    if i in "123456789":
        c+=int(i)
print(c)