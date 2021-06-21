n = int(input())
a = list(map(int,input().split()))

a = sorted(a)
b=[1]
for i in range(1,n):
    if a[i]==a[i-1]:
        b[-1]+=1
    else:
        b.append(1)

h=n
ans=0
for i in range(len(b)):
    h-=b[i]
    ans += b[i]*h
print(ans)  