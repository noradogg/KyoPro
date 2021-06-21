x=list(input())

ans=[]
i=0
while i<len(x):
    if x[i]=='.':break
    ans.append(x[i])
    i+=1
print(''.join(ans))