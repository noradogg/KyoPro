N,K=map(int,input().split())

ans=0
for n in range(1,N+1):
    ans+=100*n*K
for k in range(1,K+1):
    ans+=k*N

print(ans)