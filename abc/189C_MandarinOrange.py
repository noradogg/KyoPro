n = int(input())
a = list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(i+1,n+1):
        x = (min(a[i:j]))*(j-i)
        if x > ans:
            ans=x
print(ans)
