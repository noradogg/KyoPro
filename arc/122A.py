n=int(input())
a=list(map(int,input().split()))

if n==1:
    print(a[0])
    quit()
if n==2:
    print((a[0]*2)%(10**9+7))
    quit()

suma=sum(a)

sumodd=0
sumeven=0
for i in range(1,len(a)):
    if i%2:
        sumodd+=a[i]
    else:
        sumeven+=a[i]
sumodd%=(10**9+7)
sumeven%=(10**9+7)
ans=0
halfn=(n-1)//2
ans+=ans+sumeven*(2**(n-1-halfn))
ans+=sumodd*(2**halfn)

# a[0]の計算
ans+=a[0]*(2**(n-1-halfn))
ans+=a[0]*(2**halfn)
ans-=suma
ans%=(10**9+7)

print(ans)