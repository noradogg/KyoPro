n=int(input())

while n%10==0:
    if n==0:
        break
    n//=10

nlist=list(str(n))
flag='Yes'
for i in range(len(nlist)//2):
    if nlist[i]!=nlist[len(nlist)-i-1]:
        flag='No'
print(flag)